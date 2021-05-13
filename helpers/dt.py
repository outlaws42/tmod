from datetime import datetime, date, time
from pytz import timezone

class DT():

  def day_diff(
    month: int,
    day:int,
    year: int
    ):
    """
    Takes month day year and 
    gets the difference from
    current date
    """
    current = date.today()
    day = date(year,month,day)
    till_day = day - current
    return till_day.days

  def year_current():
    """
    Returns the current year
    """
    current = date.today()
    current_year = current.year
    return current_year

  def from_str_time_meridiem(
      str_time: str, 
      timestamp: bool = False,
      utc: bool = False, 
      tzone: str = 'US/Eastern'
      ):
      '''
      Takes a string time with AM or PM,  timestamp = True or False,
      utc = True or False, timezone = 'US/Eastern'
      timestamp = False returns datetime object today at that time,
      timestamp = True returns timestamp today at that time
      utc = True  sets timezone to UTC, False sets timezone to local timezone
      Requires from datetime import datetime, date, time / 
      from pytz import timezone
      '''
      if utc:
        tz =timezone('UTC')
      else:
        tz = timezone(tzone)
      dt_time = datetime.strptime(str_time, '%I:%M %p').time()
      dt = datetime.combine(date.today(), dt_time)
      dttz = tz.localize(dt)
      if timestamp:
        ts = int(dttz.timestamp())
        return ts
      else:
        return dttz

  def from_str_time(
      str_time: str, 
      timestamp: bool = False, 
      utc: bool = False, 
      tzone: str = 'US/Eastern'
      ):
      """ Pass string time HH:MM, timestamp = True or False,
          utc = True or False, timezone = 'US/Eastern'
          timestamp = False returns datetime object today at that time,
          timestamp = True returns timestamp today at that time
          utc = True  sets timezone to UTC, False sets timezone to local timezone
          Requires from datetime import datetime, date, time / 
          from pytz import timezone
      """
      if utc:
        tz =timezone('UTC')
      else:
        tz = timezone(tzone)

      hour, minute = str_time.split(':')
      dt = datetime.combine(date.today(),time(int(hour), int(minute)))
      dttz = tz.localize(dt)
      print(dttz)
      if timestamp:
        ts = int(dttz.timestamp())
        return ts
      else:
        return dttz

  def str_date_from_datetime(dt: datetime):
      """ Datetime return string date
          Requires from datetime import datetime
      """
      str_date = dt.strftime('%Y-%m-%d')
      return str_date

  def from_str_date(
      str_date: str,
      timestamp: bool = False,
      utc: bool = False,
      tzone: str = 'US/Eastern'
      ): 
      """ Pass string date YYYY-MM-DD, timestamp = True or False,
          utc = True or False, timezone = 'US/Eastern'
          timestamp = False returns datetime object today at that time,
          timestamp = True returns timestamp today at that time
          utc = True  sets timezone to UTC, False sets timezone to local timezone
          Requires from datetime import datetime, date, time / 
          from pytz import timezone
      """
      if utc:
        tz =timezone('UTC')
      else:
        tz = timezone(tzone)
      date_request = str_date
      year, month, day = date_request.split('-')
      dt = datetime.combine(
        date(int(year), int(month), int(day)), time())
      dttz = tz.localize(dt)
      if timestamp:
        ts = int(dttz.timestamp())
        return ts
      else:
        return dttz