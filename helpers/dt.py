from datetime import datetime, date, time
from pytz import timezone

class DT():

  def check_dt_format(self, str_date: str):
    """
    str_date = takes a string date,
    returns True or False depending if
    passed str date fits the format.
    """
    format = "%Y-%m-%d"
    try:
      dt_status = bool(datetime.strptime(str_date, format))
      return dt_status
    except ValueError as e:
      return False

  def check_dt_time(self, str_date: str):
    """
    str_date = takes a string date,
    returns True or False depending if
    passed str date fits the format.
    """
    format = "%Y-%m-%d"
    try:
      dt_status = bool(datetime.strptime(str_date, format))
      return dt_status
    except ValueError as e:
      return False


  def day_diff(
    self,
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

  def year_current(self):
    """
    Returns the current year
    """
    current = date.today()
    current_year = current.year
    return current_year

  def from_str_time_meridiem(
    self,
    str_time: str, 
    timestamp: bool = False,
    utc: bool = False, 
    tzone: str = 'US/Eastern'
    ):
    '''
    Takes a string time with AM or PM,
    str_time = "HH:MM AM" or PM   
    timestamp = True or False,
    utc = True or False, 
    timezone (default) = 'US/Eastern'
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
    try:
      dt_time = datetime.strptime(str_time, '%I:%M %p').time()
    except ValueError as e:
      return 'Time data does not match format HH:MM AM or PM'
    dt = datetime.combine(date.today(), dt_time)
    dttz = tz.localize(dt)
    if timestamp:
      ts = int(dttz.timestamp())
      return ts
    else:
      return dttz

  def from_str_time(
    self,
    str_time: str, 
    timestamp: bool = False, 
    utc: bool = False, 
    tzone: str = 'US/Eastern'
    ):
    """ 
    str_time = "HH:MM" based 24 hour clock, 
    timestamp = True or False,
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
    if timestamp:
      ts = int(dttz.timestamp())
      return ts
    else:
      return dttz

  def str_date_from_datetime(self,dt: datetime):
    """ Datetime return string date
        Requires from datetime import datetime
    """
    str_date = dt.strftime('%Y-%m-%d')
    return str_date

  def from_str_date(
    self,
    str_date: str,
    timestamp: bool = False,
    utc: bool = False,
    tzone: str = 'US/Eastern'
    ): 
    """ Pass string date YYYY-MM-DD, timestamp = True or False,
        utc = True or False, timezone = 'US/Eastern'
        timestamp = False returns datetime object current time at that date,
        timestamp = True returns timestamp current time at that date
        utc = True  sets timezone to UTC, False sets timezone to local timezone
        Requires from datetime import datetime, date, time / 
        from pytz import timezone
    """
    dt_validation = self.check_dt_format(str_date)
    if dt_validation == False:
      message = ( f'This is not a correct date string ' 
      f'following YYYY-MM-DD You entered {str_date}')
      return message
    if utc:
      tz =timezone('UTC')
    else:
      tz = timezone(tzone)
    date_request = str_date
    year, month, day = date_request.split('-')
    tm = datetime.now(tz).time()
    dt = datetime.combine(
      date(int(year), int(month), int(day)), tm)
    dttz = tz.localize(dt)
    if timestamp:
      ts = int(dttz.timestamp())
      return ts
    else:
      return dttz

if __name__ == "__main__":
  app = DT()
  test = app.from_str_time(str_time = '05:30 AM')
  print(test)