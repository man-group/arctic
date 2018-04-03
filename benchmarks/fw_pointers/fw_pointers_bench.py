import os
import logging
import random
from collections import namedtuple
from pprint import pprint

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pymongo import ASCENDING, DESCENDING

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
        lib.write(sym_name + '_ids', data_df if data_df is not None else get_random_df(nrows, ncols), fw_pointers=WITH_ID)
        lib.write(sym_name + '_shas', data_df if data_df is not None else get_random_df(nrows, ncols), fw_pointers=WITH_SHA)
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


def setup_auth(username, password):
    register_get_auth_hook(lambda host, app_name, database_name: AuthCreds(username, password))
