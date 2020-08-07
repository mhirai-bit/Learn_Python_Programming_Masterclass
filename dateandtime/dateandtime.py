import time

print("The epoch of this system starts at " + time.strftime("%c", time.gmtime(0)))

print("The current timezone is {0} with an offset of {1}".format((time.tzname[0], time.timezone)))

if time.daylight != 0:
    print("\tDaylight Saing Time is in effect for this location")
    print("\tThe DST timezone is " + time.tzname[1])

print("local time is " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))