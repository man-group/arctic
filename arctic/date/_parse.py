from dateutil.parser import parse as _parse


def parse(string, agnostic=False, **kwargs):
    return _parse(string, yearfirst=True, dayfirst=False, **kwargs)
