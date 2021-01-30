```shell
...
================================================================================
=================================== FAILURES ===================================
...
================================================================================
=========================== short test summary info ============================
FAILED tests/integration/tickstore/test_toplevel.py::test_should_return_data_when_date_range_falls_in_a_single_underlying_library
FAILED tests/integration/tickstore/test_toplevel.py::test_should_return_data_when_date_range_spans_libraries_even_if_one_returns_nothing
FAILED tests/integration/tickstore/test_toplevel.py::test_should_write_top_level_with_list_of_dicts
FAILED tests/integration/tickstore/test_toplevel.py::test_should_write_top_level_with_correct_timezone
FAILED tests/unit/store/test_version_store_audit.py::test_ArcticTransaction_detects_concurrent_writes

================================================================================

= 5 failed, 1307 passed, 18 skipped, 8 xfailed, 1 xpassed, 60744 warnings in 1323.29s (0:22:03) =
The command "python setup.py test --pytest-args=-v" exited with 1.
1.26s$ pycodestyle arctic
The command "pycodestyle arctic" exited with 0.
```