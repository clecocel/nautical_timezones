A simple tool to convert a timestamp to a datetime in the local nautical timezone.

Nautical timezones information:
- https://en.wikipedia.org/wiki/Nautical_time
- https://en.wikipedia.org/wiki/Time_zone#Nautical_time_zones
- https://en.wikipedia.org/wiki/List_of_UTC_time_offsets

# Usage
Example usage:
```
import time
from nautical_timezone_converter.converter import utc_to_nautical_time
t = time.time()
dt = utc_to_nautical_time(t, 120)
print (dt)
dt.tzname()
dt.utcoffset()
```
