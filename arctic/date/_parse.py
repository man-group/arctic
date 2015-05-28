from dateutil.parser import parse as _parse


def parse(string, agnostic=False, **kwargs):
    parsed = _parse(string, **kwargs)
    if agnostic or (parsed == _parse(string, yearfirst=True, **kwargs)
                           == _parse(string, dayfirst=True, **kwargs)):
        return parsed
    else:
        raise ValueError("The date was ambiguous: %s" % string)
