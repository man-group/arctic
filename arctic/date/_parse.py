"""
Copyright (C) 2020 Man Group
For a list of authors, see README.md; for the license, see file LICENSE in project root directory.
"""
from dateutil.parser import parse as _parse


def parse(string, agnostic=False, **kwargs):
    return _parse(string, yearfirst=True, dayfirst=False, **kwargs)
