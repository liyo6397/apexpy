from apexpy import Apex
import datetime as dt
atime = dt.datetime(2015, 2, 10, 18, 0, 0)
apex15 = Apex(date=2015.3)  # dt.date and dt.datetime objects also work

# Geodetic to apex, scalar input
mlat, mlon = apex15.convert(60, 15, 'geo', 'apex', height=300)
print("{:.12f}, {:.12f}".format(mlat, mlon))

# Apex to geodetic, array input
glat, glon = apex15.convert([90, -90], 0, 'apex', 'geo', height=0)
print(["{:.12f}, {:.12f}".format(ll, glon[i]) for i,ll in enumerate(glat)])

# Geodetic to magnetic local time
mlat, mlt = apex15.convert(60, 15, 'geo', 'mlt', datetime=atime)
print("{:.12f}, {:.12f}".format(mlat, mlt))

# can also convert magnetic longitude to mlt
mlt = apex15.mlon2mlt(120, atime)
print("{:.2f}".format(mlt))

