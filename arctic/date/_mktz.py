import bisect
import os
import dateutil
import tzlocal


class TimezoneError(Exception):
    pass


def mktz(zone=None):
    """
    Return a new timezone (tzinfo object) based on the zone using the python-dateutil
    package.

    The concise name 'mktz' is for convenient when using it on the
    console.

    Parameters
    ----------
    zone : `String`
           The zone for the timezone. This defaults to local, returning:
           tzlocal.get_localzone()

    Returns
    -------
    An instance of a timezone which implements the tzinfo interface.

    Raises
    - - - - - -
    TimezoneError : Raised if a user inputs a bad timezone name.
    """
    if zone is None:
        zone = tzlocal.get_localzone().zone
    tz = dateutil.tz.gettz(zone)
    if not tz:
        raise TimezoneError('Timezone "%s" can not be read' % (zone))
    return tz
