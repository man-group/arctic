"""
Copyright (C) 2020 Man Group
For a list of authors, see README.md; for the license, see file LICENSE in project root directory.
"""
import warnings

# Turn deprecation warnings into errors
warnings.simplefilter('error', DeprecationWarning)

pytest_plugins = ['arctic.fixtures.arctic']
