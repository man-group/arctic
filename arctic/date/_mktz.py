import bisect
import os
import dateutil
import tzlocal

DEFAULT_TIME_ZONE_NAME = tzlocal.get_localzone().zone  # 'Europe/London'
TIME_ZONE_DATA_SOURCE = '/usr/share/zoneinfo/'


class TimezoneError(Exception):
    pass


class tzfile(dateutil.tz.tzfile):

    def _find_ttinfo(self, dtm, laststd=0):
        """Faster version of parent class's _find_ttinfo() as this uses bisect rather than a linear search."""
        if dtm is None:
            # This will happen, for example, when a datetime.time object gets utcoffset() called.
            raise ValueError('tzinfo object can not calculate offset for date %s' % dtm)
        ts = ((dtm.toordinal() - dateutil.tz.EPOCHORDINAL) * 86400
                     + dtm.hour * 3600
                     + dtm.minute * 60
                     + dtm.second)
        idx = bisect.bisect_right(self._trans_list, ts)
        if len(self._trans_list) == 0 or idx == len(self._trans_list):
            return self._ttinfo_std
        if idx == 0:
            return self._ttinfo_before
        if laststd:
            while idx > 0:
                tti = self._trans_idx[idx - 1]
                if not tti.isdst:
                    return tti
                idx -= 1
            else:
                return self._ttinfo_std
        else:
            return self._trans_idx[idx - 1]


def mktz(zone=None):
    """
    Return a new timezone based on the zone using the python-dateutil
    package.  This convenience method is useful for resolving the timezone
    names as dateutil.tz.tzfile requires the full path.

    The concise name 'mktz' is for convenient when using it on the
    console.

    Parameters
    ----------
    zone : `String`
           The zone for the timezone. This defaults to 'local'.

    Returns
    -------
    An instance of a timezone which implements the tzinfo interface.

    Raises
    - - - - - -
    TimezoneError : Raised if a user inputs a bad timezone name.
    """

    if zone is None:
        zone = DEFAULT_TIME_ZONE_NAME
    _path = os.path.join(TIME_ZONE_DATA_SOURCE, zone)
    try:
        tz = tzfile(_path)
    except (ValueError, IOError) as err:
        raise TimezoneError('Timezone "%s" can not be read, error: "%s"' % (zone, err))
    # Stash the zone name as an attribute (as pytz does)
    tz.zone = zone if not zone.startswith(TIME_ZONE_DATA_SOURCE) else zone[len(TIME_ZONE_DATA_SOURCE):]
    return tz
