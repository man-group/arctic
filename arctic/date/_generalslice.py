from enum import Enum


class Intervals(Enum):
    (OPEN_CLOSED, CLOSED_OPEN, OPEN_OPEN, CLOSED_CLOSED) = range(1101, 1105)
(OPEN_CLOSED, CLOSED_OPEN, OPEN_OPEN, CLOSED_CLOSED) = INTERVALS = Intervals.__members__.values()


class GeneralSlice(object):
    """General slice object, supporting open/closed ranges:

    =====  ====  ============================  ===============================
    start  end  interval                      Meaning
    -----  ----  ----------------------------  -------------------------------
    None   None                                any item
    a      None  CLOSED_CLOSED or CLOSED_OPEN  item >= a
    a      None  OPEN_CLOSED or OPEN_OPEN      item > a
    None   b     CLOSED_CLOSED or OPEN_CLOSED  item <= b
    None   b     CLOSED_OPEN or OPEN_OPEN      item < b
    a      b     CLOSED_CLOSED                 item >= a and item <= b
    a      b     OPEN_CLOSED                   item > a and item <= b
    a      b     CLOSED_OPEN                   item >= a and item < b
    a      b     OPEN_OPEN                     item > a and item < b
    =====  ====  ============================  ===============================
    """

    def __init__(self, start, end, step=None, interval=CLOSED_CLOSED):
        self.start = start
        self.end = end
        self.step = step
        self.interval = interval

    @property
    def startopen(self):
        """True if the start of the range is open (item > start),
        False if the start of the range is closed (item >= start)."""
        return self.interval in (OPEN_CLOSED, OPEN_OPEN)

    @property
    def endopen(self):
        """True if the end of the range is open (item < end),
        False if the end of the range is closed (item <= end)."""
        return self.interval in (CLOSED_OPEN, OPEN_OPEN)
