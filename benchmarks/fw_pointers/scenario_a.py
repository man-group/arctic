import os

from fw_pointers_bench import do_benchmark, IndexSpec, setup_auth, ASCENDING, DESCENDING, WITH_ID, WITH_SHA, LEGACY


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
                'fw_pointer_types': (LEGACY, ),
                'component': ['total', 'read', 'createNumPy', 'decompress'],
                'title_prefix': 'Breakdown'
            }
        ]
    }

    # Configure authentication
    setup_auth('user', 'password')

    # Run the benchmark
    do_benchmark(
        mongo_host='localhost:27217',  # single ram disk
        desc='Deleteme',
        config=scenario_config,
        quota=21.0,
        force_drop=False,
        populate_existing_data=True,
        save_figure=True,
        # drop_indexes=[
        #     # IndexSpec(keys=[('symbol', ASCENDING), ('sha', ASCENDING), ('segment', ASCENDING)], unique=True, background=True),
        #     # IndexSpec(keys=[('symbol', ASCENDING), ('_id', ASCENDING), ('segment', ASCENDING)], unique=True, background=True),
        # ],
        # create_indexes=[
        #     # IndexSpec(keys=[('symbol', ASCENDING), ('sha', ASCENDING), ('segment', ASCENDING)], unique=True, background=True),
        #     # IndexSpec(keys=[('symbol', ASCENDING), ('_id', ASCENDING), ('segment', ASCENDING)], unique=True, background=True)
        # ],
        exit_after_init=False
    )


if __name__ == '__main__':
    main()
