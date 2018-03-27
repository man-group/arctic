import arctic
import pandas as pd
import numpy as np
import random
from pandas.util.testing import assert_frame_equal, assert_series_equal
import logging

from arctic.store.fw_pointers import WITH_ID, WITH_SHA, LEGACY

logging.basicConfig(level=logging.INFO)
from arctic.hooks import register_get_auth_hook

import matplotlib.pyplot as plt

from collections import namedtuple

import os
from pprint import pprint

# To auth with user/password when using  cluster
AuthCreds = namedtuple('AuthCreds', 'user password')
register_get_auth_hook(lambda host, app_name, database_name: AuthCreds('user', 'password'))


def get_random_df(nrows, ncols):
    ret_df = pd.DataFrame(np.random.randn(nrows, ncols),
                          index=pd.date_range('20170101',
                                              periods=nrows, freq='S'),
                          columns=["".join([chr(random.randint(ord('A'), ord('Z'))) for _ in range(8)]) for _ in
                                   range(ncols)])
    ret_df.index.name = 'index'
    ret_df.index = ret_df.index.tz_localize('UTC')
    return ret_df


def initialize_library(mongo_host, lib_name='test_lib', init_quota=None, force_drop=False):
    at = arctic.Arctic('mongodb://' + mongo_host)  # single on ramdisk
    if force_drop:
        at.delete_library(lib_name)
        at.initialize_library(lib_name, arctic.VERSION_STORE, segment='month')

    lib = at.get_library(lib_name)

    if init_quota:
        at.set_quota(lib_name, int(init_quota*1024**3))

    return lib


def populate_with_existing_data(lib, num_existing_symbols, df_rows=None, df_cols=None, data_df=None, base_sym_name='existing_sym'):
    logging.info('Populate with existing documents')
    for i in range(num_existing_symbols):
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


def main():
    # mongo_host = 'dpediaditakis.hn.ada.res.ahl:27017'  # cluster
    # mongo_host = 'dpediaditakis.hn.ada.res.ahl:27117'  # single
    mongo_host = 'dpediaditakis.hn.ada.res.ahl:27217'  # single ram disk
    desc = 'Mongo RamDisk Single'
    fig_save_path = os.path.join('/users/is/dpediaditakis/Documents/results_arctic', desc.replace(' ', '_'))
    if not os.path.exists(fig_save_path):
        os.makedirs(fig_save_path)


    # lib = initialize_library(mongo_host, lib_name='test_lib', init_quota=5.0, force_drop=True)
    # populate_with_existing_data(lib,
    #                             num_existing_symbols=100000,
    #                             base_sym_name='existing_sym_c',
    #                             # df_rows=10*20000, df_cols=12,
    #                             # data_df=get_random_df(10*20000, 12)
    #                             data_df=get_random_df(100, 12)
    #                             )

    lib = initialize_library(mongo_host, lib_name='test_lib', init_quota=21.0)

    test_syms = get_test_symbols(num_symbols=100, base_sym_name='sym')

    iterations = 10
    do_legacy, do_with_ids, do_with_shas = True, True, True
    for num_rows in (100, 5000, 1*20000, 10*20000, 50*20000):
        write_test_symbols(lib, test_syms,
                       # nrows=100, ncols=16,
                       # data_df=get_random_df(2 * 20000, 12)
                       data_df=get_random_df(num_rows, 12)
                       # data_df=get_random_df(20*20000, 12)
                       )
        reset_experiment()

        run_experiment(lib, test_syms, num_iterations=iterations,
                       do_legacy=do_legacy, do_with_ids=do_with_ids, do_with_shas=do_with_shas)

        plot_results(fw_pointer_types=(WITH_ID, WITH_SHA, LEGACY),
                     component=['read'],
                     title='Comparison {} \n[read] \n({} rows) \n({})'.format((WITH_ID, WITH_SHA, LEGACY), num_rows, desc),
                     save_figure_path=fig_save_path
                     )

        plot_results(fw_pointer_types=(LEGACY, ),
                     component=['total', 'read', 'createNumPy', 'decompress'],
                     title='Breakdown {} \n[{}] \n({} rows) \n({})'.format(LEGACY, ('total', 'read', 'createNumPy', 'decompress'), num_rows, desc),
                     save_figure_path=fig_save_path
                     )


if __name__ == '__main__':
    main()
