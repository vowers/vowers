import time
from datetime import datetime

# 把datetime转成字符串


def datetime_toString(dt, fmt='%Y%m%d%H%M'):
    return dt.strftime(fmt)

# 把字符串转成datetime


def string_toDatetime(string, fmt='%Y%m%d%H%M'):
    return datetime.strptime(string, fmt)

# 把字符串转成时间戳形式


def string_toTimestamp(strTime):
    return time.mktime(string_toDatetime(strTime).timetuple())

# 把时间戳转成字符串形式


def timestamp_toString(stamp, fmt='%Y%m%d%H%M'):
    return time.strftime(fmt, time.localtime(stamp))

# 把datetime类型转外时间戳形式


def datetime_toTimestamp(dateTim):
    return time.mktime(dateTim.timetuple())

# 返回一段时间list


def date_range(beg, end, multiple, fmt='%Y%m%d%H%M'):
    beg = int(time.mktime(time.strptime(beg, fmt)))
    end = int(time.mktime(time.strptime(end, fmt)))
    return [time.strftime(fmt, time.localtime(i)) for i in range(beg, end+1, 60*multiple)]
