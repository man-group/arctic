import os
import logging
import random
from collections import namedtuple
from pprint import pprint

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pymongo import ASCENDING

import arctic
from arctic.store.fw_pointers import WITH_ID, WITH_SHA, LEGACY, do_drop_index, do_create_index, IndexSpec
from arctic.hooks import register_get_auth_hook

logging.basicConfig(level=logging.INFO)

# To auth with user/password when using  cluster
AuthCreds = namedtuple('AuthCreds', 'user password')


def get_random_df(nrows, ncols):
    ret_df = pd.DataFrame(np.random.randn(nrows, ncols),
                          index=pd.date_range('20170101',
                                              periods=nrows, freq='S'),
                          columns=["".join([chr(random.randint(ord('A'), ord('Z'))) for _ in range(8)]) for _ in
                                   range(ncols)])
    ret_df.index.name = 'index'
    ret_df.index = ret_df.index.tz_localize('UTC')
    return ret_df


def initialize_library(mongo_host, lib_name='test_lib', init_quota=None, force_data_drop=False, 
                       drop_indexes=None, create_indexes=None):
    at = arctic.Arctic('mongodb://' + mongo_host)  # single on ramdisk
    if force_data_drop:
        at.delete_library(lib_name)
        at.initialize_library(lib_name, arctic.VERSION_STORE, segment='month')

    lib = at.get_library(lib_name)

    for idx_spec in (drop_indexes if drop_indexes else []):
        do_drop_index(lib._collection, idx_spec)

    for idx_spec in (create_indexes if create_indexes else []):
        do_create_index(lib._collection, idx_spec)

    if init_quota:
        at.set_quota(lib_name, int(init_quota*1024**3))

    return lib


def populate_with_existing_data(lib, num_existing_symbols, df_rows=None, df_cols=None, data_df=None,
                                base_sym_name='existing_sym', do_print=False):
    logging.info('Populate with existing documents')
    for i in range(num_existing_symbols):
        if do_print:
            logging.info('writting dataframe {} of {}'.format(i, num_existing_symbols))
        lib.write("{}_{}".format(base_sym_name, i), data_df if data_df is not None else get_random_df(df_rows, df_cols))
    logging.info('Done populating with existing documents')


def reset_experiment():
    arctic.store._ndarray_store.NdarrayStore.reset_measurements()


def get_test_symbols(num_symbols, base_sym_name='sym'):
    return ["{}_{}".format(base_sym_name, i) for i in range(num_symbols)]


def write_test_symbols(lib, test_symbols, nrows=None, ncols=None, data_df=None):
    logging.info('Populating the test symbols')
    for sym_name in test_symbols:
        lib.write(sym_name + '_ids', data_df if data_df is not None else get_random_df(nrows, ncols), fw_pointers=arctic.store.fw_pointers.WITH_ID)
        lib.write(sym_name + '_shas', data_df if data_df is not None else get_random_df(nrows, ncols), fw_pointers=arctic.store.fw_pointers.WITH_SHA)
        lib.write(sym_name, data_df if data_df is not None else get_random_df(nrows, ncols))
    logging.info('Done populating the test symbols')


def run_experiment(lib, test_symbols, num_iterations, do_legacy=True, do_with_ids=True, do_with_shas=True):
    logging.info('Start the reads')
    for x in range(num_iterations):
        round = '{} of {}'.format(x, num_iterations)

        if do_legacy:
            logging.info('No fw_pointer reads ({})'.format(round))
            for sym_name in test_symbols:
                lib.read(sym_name)

        if do_with_ids:
            logging.info('fw_pointer with IDs reads ({})'.format(round))
            for sym_name in test_symbols:
                lib.read(sym_name + '_ids')

        if do_with_shas:
            logging.info('fw_pointer with SHAs reads ({})'.format(round))
            for sym_name in test_symbols:
                lib.read(sym_name + '_shas')
    logging.info('Done with reads')


def print_stats(stats, id):
    print "Stats for {}: \n\tMin={}\n\tMax={}\n\tMean={}\n\tStdev={}".format(
        id, np.min(stats), np.max(stats), np.mean(stats), np.std(stats))


def plot_results(fw_pointer_types, component, title, save_figure_path=None):
    logging.info('Plotting')
    plt.clf()
    # Print the stats
    markers = ['>', '*', '^', '<']
    i = 0
    pprint(arctic.store._ndarray_store.NdarrayStore.MEASUREMENTS)
    for k, stats in arctic.store._ndarray_store.NdarrayStore.MEASUREMENTS.iteritems():
        if not [x for x in fw_pointer_types if x in k]:
            continue

        if not [x for x in component if x in k]:
            continue

        print_stats(stats, k)

        hist, x = np.histogram(stats, bins=20)
        y = np.cumsum(hist)
        plt.plot(x[1:], y, label=k, linewidth=1.5, marker=markers[i % len(markers)], markersize=4)
        i += 1

    if i == 0:
        return

    plt.legend(loc='lower right')
    plt.title(title, fontsize=12)
    x1, x2, y1, y2 = plt.axis()
    plt.axis((x1, x2, 0, y2*1.05))

    plt.tight_layout()

    if save_figure_path is not None:
        fname = os.path.join(save_figure_path, title.replace(' ', '_') + ".pdf")
        plt.savefig(fname, dpi=120)
    else:
        plt.show()


DEFAULT_PLOT_CONFIG = {
    'fw_pointer_types': (LEGACY,),
    'component': ('read',),
    'title_prefix': 'Only Arctic read'
}


def do_benchmark(mongo_host, desc, config, quota, force_drop, populate_existing_data, save_figure,
                 drop_indexes=None, create_indexes=None, exit_after_init=False):
    fig_save_path = None
    if save_figure:
        fig_save_path = os.path.join('/users/is/dpediaditakis/Documents/results_arctic', desc.replace(' ', '_'))
        if not os.path.exists(fig_save_path):
            os.makedirs(fig_save_path)

    lib = initialize_library(mongo_host, lib_name='test_lib', init_quota=quota, force_data_drop=bool(force_drop),
                             drop_indexes=drop_indexes, create_indexes=create_indexes)

    if populate_existing_data:
        # Some large
        populate_with_existing_data(lib,
                                    num_existing_symbols=config.get('existing_large_num', 100),
                                    base_sym_name='existing_sym_large',
                                    data_df=get_random_df(*config.get('existing_large_dim', (2*20000, 12))),
                                    do_print=True
                                    )
        # Many small
        populate_with_existing_data(lib,
                                    num_existing_symbols=config.get('existing_small_num', 5000),
                                    base_sym_name='existing_sym_small',
                                    data_df=get_random_df(*config.get('existing_small_dim', (100, 12)))
                                    )
    # Stop here if flag is set, after initializing library and populating witht he existing data
    if exit_after_init:
        return

    test_syms = get_test_symbols(num_symbols=config.get('test_syms_num', 10), base_sym_name='sym')

    for num_rows in config.get('test_syms_rows', (100, 5000, 2*20000)):
        write_test_symbols(lib, test_syms,
                           data_df=get_random_df(num_rows, config.get('test_syms_cols', 12)))
        reset_experiment()

        run_experiment(lib, test_syms,
                       num_iterations=config.get('iterations', 1),
                       do_legacy=config.get('do_legacy', True),
                       do_with_ids=config.get('do_with_ids', True),
                       do_with_shas=config.get('do_with_shas', True))
        
        for plot_config in config.get('plots', (DEFAULT_PLOT_CONFIG,)):
            fw_ptrs = plot_config.get('fw_pointer_types', (LEGACY,))
            component = plot_config.get('component', ('read',))
            title_prefix = plot_config.get('title_prefix', '')
            plot_results(fw_pointer_types=fw_ptrs,
                         component=component,
                         title='{} {} \n[read] \n({} rows) \n({})'.format(title_prefix, fw_ptrs, num_rows, desc),
                         save_figure_path=fig_save_path)


def main():
    # Specify the scenario of the experiment
    scenario_config = {
        'fig_path': os.path.join(os.path.expanduser('~'), 'Documents', 'results_arctic'),

        # Existing Data
        'existing_large_num': 1,
        'existing_large_dim': (10 * 20000, 12),
        'existing_small_num': 20,
        'existing_small_dim': (100, 12),

        # Experiment symbols
        'test_syms_num': 1,
        'test_syms_rows': (100,),  # 5000 , 1 * 20000, 10 * 20000, 25 * 20000),
        'test_syms_cols': 12,

        # Number of iterations
        'iterations': 10,

        # Experiment read implementation
        'do_legacy': True,
        'do_with_ids': True,
        'do_with_shas': True,

        # Plotting options
        'plots': [
            {
                'fw_pointer_types': (WITH_ID, WITH_SHA, LEGACY),
                'component': ['read'],
                'title_prefix': 'Comparison'
            },
            {
                'fw_pointer_types': (LEGACY),
                'component': ['total', 'read', 'createNumPy', 'decompress'],
                'title_prefix': 'Breakdown'
            }
        ]
    }

    # Configure authentication
    register_get_auth_hook(lambda host, app_name, database_name: AuthCreds('user', 'password'))
    # register_get_auth_hook(lambda host, app_name, database_name: AuthCreds('admin', '???????'))

    # Run the benchmark
    do_benchmark(
        mongo_host='localhost:27217',  # single ram disk
        desc='Deleteme',
        config=scenario_config,
        quota=21.0,
        force_drop=False,
        populate_existing_data=True,
        save_figure=True,
        drop_indexes=[
            IndexSpec(keys=[('symbol', ASCENDING), ('sha', ASCENDING), ('segment', ASCENDING)], unique=True, background=True),
            IndexSpec(keys=[('symbol', ASCENDING), ('_id', ASCENDING), ('segment', ASCENDING)], unique=True, background=True),
        ],
        create_indexes=[
            IndexSpec(keys=[('symbol', ASCENDING), ('sha', ASCENDING), ('segment', ASCENDING)], unique=True, background=True),
            # IndexSpec(keys=[('symbol', ASCENDING), ('_id', ASCENDING), ('segment', ASCENDING)], unique=True, background=True)
        ],
        exit_after_init=False
    )


if __name__ == '__main__':
    main()



# mongo_host = '0.switch.research.mongo.res.ahl:27017'  # research cluster
# desc = 'Research Mongo Cluster'

# mongo_host = 'dlondbahls80:27201'  # new dev cluster
# desc = 'Dev Mongo Cluster'

# mongo_host = 'dpediaditakis.hn.ada.res.ahl:27017'  # local cluster
# desc = 'Mongo iscsi Cluster'

# mongo_host = 'dpediaditakis.hn.ada.res.ahl:27117'  # single
# desc = 'Mongo iscsi Single'

# mongo_host = 'dpediaditakis.hn.ada.res.ahl:27217'  # single ram disk
# desc = 'Mongo RamDisk Single'


# import time
# import numpy as np
# import pymongo
# from ahl.mongo import Mongoose
#
# WITH_ID = 'fw_pointers_with_id'
# WITH_SHA = 'fw_pointers_with_sha'
#
# def build_query(lib, symbol):
#     version = lib._versions.find_one({'symbol': symbol}, sort=[('version', pymongo.DESCENDING)])
#     query = {'symbol': symbol}
#     if WITH_ID in version:
#         query['_id'] = {'$in': version[WITH_ID]}
#     elif WITH_SHA in version:
#         query['sha'] = {'$in': version[WITH_SHA]}
#     else:
#         query['parent'] = version.get('base_version_id', version['_id'])
#     query['segment'] = {'$lt': version['up_to']}
#     return query
#
#
# def bench_sym(lib, symbol, iterations=100):
#     query = build_query(lib, symbol)
#     measurements = []
#     for i in range(iterations):
#         start = time.time()
#         cursor = lib._collection.find(query, sort=[('segment', pymongo.ASCENDING)])
#         res = list(cursor)
#         delta = time.time() - start
#         measurements.append(delta)
#         # print len(res)
#     print "\n\n{0}\nMean={1:.4f}\nStdev={2:.4f}\nMin={3:.4f}\nMax={4:.4f}".format(symbol,
#                                                                                   np.mean(measurements),
#                                                                                   np.std(measurements),
#                                                                                   np.min(measurements),
#                                                                                   np.max(measurements))


# tdinew_res = Mongoose('research')['oneminute.TDI1MIN_NEW']
# # symbol = 'FUT_FTL_200112_DIMOS'
# # syms = tdinew_res.list_symbols()
# # symbol = syms[0]
#
# bench_sym(tdinew_res, 'FUT_FTL_200112_DIMOS', iterations=500)
# bench_sym(tdinew_res, 'FUT_FTL_200112_DIMOS_SHA', iterations=500)
# bench_sym(tdinew_res, 'FUT_FTL_200112', iterations=500)





# import arctic
# import pymongo
# from collections import namedtuple
# from arctic.hooks import register_get_auth_hook
# from pprint import pprint
# from ahl.mongo.auth import get_auth
#
#
# # register_get_auth_hook(get_auth)
# # lib = Mongoose('research')['oneminute.TDI1MIN_NEW']
# # symbol = 'FUT_FTL_200112'
# # symbol = 'FUT_FTL_200112_DIMOS'
# # symbol = 'FUT_FTL_200112_DIMOS_SHA'
#
# # To auth with user/password when using  cluster
# AuthCreds = namedtuple('AuthCreds', 'user password')
# register_get_auth_hook(lambda host, app_name, database_name: AuthCreds('user', 'password'))
# at = arctic.Arctic('mongodb://localhost:27217')
# lib = at['test_lib']
# symbol = 'sym_0_ids'
# query = build_query(lib, symbol)
# expl = lib._collection.find(query, sort=[('segment', pymongo.ASCENDING)]).explain()
# pprint(expl['queryPlanner'])
#
# bench_sym(lib, 'sym_0', iterations=5000)
# bench_sym(lib, 'sym_0_ids', iterations=5000)
# bench_sym(lib, 'sym_0_shas', iterations=5000)
#
