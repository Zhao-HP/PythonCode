from datetime import timedelta, date
import datetime


# 获取当前日期
def today():
    return date.today()


# 将指定日期转换为字符串
def dateToStr(date, dateStr):
    return datetime.datetime.strftime(date, dateStr)


# 将当前日期以【yyyyMMdd】形式返回
def todayStr():
    return dateToStr(datetime.date.today(), "%Y%m%d")


# 获取指定日期的结束时间【23:59:59】
def endOfDay(date):
    return datetime.datetime(date.year, date.month, date.day, 23, 59, 59)


# 获取指定日期的开始时间【00:00:00】
def startOfDay(date):
    return datetime.datetime(date.year, date.month, date.day, 00, 00, 00)


# 将指定日期加上指定天数，n为负数表示减去多少天
def addDays(date, n=0):
    return date + timedelta(days=n)


# 将指定日期加上指定天数，返回当天最后一秒
def addAndEndDays(date, n=0):
    return endOfDay(addDays(date, n))


# 将指定日期加上指定天数，返回当天第一秒
def addAndStartDays(date, n=0):
    return startOfDay(addDays(date, n))


# 返回指定日期所在周的星期天的最后一秒
def endOfWeekday(date):
    weekday = date.isoweekday()
    return addAndEndDays(date, 7 - weekday)


# 返回指定日期所在周的星期一的第一秒
def startOfWeekday(date):
    weekday = date.isoweekday()
    return addAndStartDays(date, -(weekday - 1))


def parseDateStr(dateStr):
    return datetime.datetime.strptime(dateStr, '%Y-%m-%d %H:%M:%S')
