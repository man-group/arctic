import bisect
import os
import dateutil
import tzlocal
import six


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
    zone = six.u(zone)
    tz = dateutil.tz.gettz(zone)
    if not tz:
        raise TimezoneError('Timezone "%s" can not be read' % (zone))
    # Stash the zone name as an attribute (as pytz does)
    if not hasattr(tz, 'zone'):
        tz.zone = zone
        for p in dateutil.tz.TZPATHS:
            if zone.startswith(p):
                tz.zone = zone[len(p) + 1:]
                break
    return tz
