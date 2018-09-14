#!/usr/bin/env python

import datetime


class FixedOffset(datetime.tzinfo):
    """Fixed offset in hours east from UTC."""

    def __init__(self, offset, name):
        self.__offset = datetime.timedelta(hours=offset)
        self.__name = name

    def utcoffset(self, dt):
        return self.__offset

    def tzname(self, dt):
        return self.__name

    def dst(self, dt):
        return datetime.timedelta(0)


nautical_timezones = {
    1: FixedOffset(1, "A"),
    2: FixedOffset(2, "B"),
    3: FixedOffset(3, "C"),
    4: FixedOffset(4, "D"),
    5: FixedOffset(5, "E"),
    6: FixedOffset(6, "F"),
    7: FixedOffset(7, "G"),
    8: FixedOffset(8, "H"),
    9: FixedOffset(9, "I"),
    10: FixedOffset(10, "K"),
    11: FixedOffset(11, "L"),
    12: FixedOffset(12, "M"),
    -1: FixedOffset(-1, "N"),
    -2: FixedOffset(-2, "O"),
    -3: FixedOffset(-3, "P"),
    -4: FixedOffset(-4, "Q"),
    -5: FixedOffset(-5, "R"),
    -6: FixedOffset(-6, "S"),
    -7: FixedOffset(-7, "T"),
    -8: FixedOffset(-8, "U"),
    -9: FixedOffset(-9, "V"),
    -10: FixedOffset(-10, "W"),
    -11: FixedOffset(-11, "X"),
    -12: FixedOffset(-12, "Y"),
    0: FixedOffset(0, "Z")}


def utc_to_nautical_time(timestamp, longitude):
    time_diff = int(round(longitude / 15.))
    tz = nautical_timezones[time_diff]
    t = datetime.datetime.fromtimestamp(timestamp, tz)
    return t


if __name__ == "__main__":
    pass
