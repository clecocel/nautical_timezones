#!/usr/bin/env python

from nautical_timezone_converter.converter import utc_to_nautical_time


def test_utc_to_nautical_time():
    timestamp = 1535916764.625136
    # Convert timestamp to nautical time in SF - longitude is -122.5
    dt = utc_to_nautical_time(timestamp, -122.5)
    assert dt.tzname() == "U"
    assert (dt.year == 2018 and dt.month == 9 and dt.day == 2 and
            dt.hour == 11 and dt.minute == 32 and dt.second == 44)

    # Convert timestamp to nautical time in Berlin - longitude is 13.4
    dt = utc_to_nautical_time(timestamp, 13.4)
    assert dt.tzname() == "A"
    assert (dt.year == 2018 and dt.month == 9 and dt.day == 2 and
            dt.hour == 20 and dt.minute == 32 and dt.second == 44)
