#! /usr/bin/env python3

# -*- coding: utf-8 -*-
version = '2021-04-16'

# Imports included with python
import random
import os
import os.path
import sys
from datetime import datetime, date, time, timezone, tzinfo
from collections import ChainMap # Requires python 3.3
import json

# Imports installed through pip
try:
  # pip install pyyaml if needed
  import yaml
except:
  pass

try:
  # pip install pytz if needed
  import pytz
except:
  pass

try:
  # pip install requests if needed
  import requests
except:
  pass

try:
  # pip install beautifulsoup4 if needed
  from bs4 import BeautifulSoup  
except:
  pass

# File I/O /////////////////////////////////////////
def get_resource_path(rel_path):
    dir_of_py_file = os.path.dirname(sys.argv[0])
    rel_path_to_resource = os.path.join(dir_of_py_file, rel_path)
    abs_path_to_resource = os.path.abspath(rel_path_to_resource)
    return abs_path_to_resource

def open_file(
    fname: str,
    fdest: str = 'relative', 
    def_content: str = '0'
    ):
    """
    fname = filename, fdest = file destination, 
    def_content = default value if the file doesn't exist
    opens the file if it exists and returns the contents
    if it doesn't exitst it creates it writes 
    the def_content value to it and returns the def_content value
    import os
    """
    home = os.path.expanduser("~")
    try:
        if fdest == 'home' or fdest == 'Home':
            with open(f'{home}/{fname}', 'r') as path_text:
                content=path_text.read()
        else:
            with open(get_resource_path(fname), 'r') as text:
                content=text.read()
        return content
    except(FileNotFoundError) as e:
        print(e)
        print('It is reading here')
        if fdest == 'home' or fdest == 'Home':
            with open(f'{home}/{fname}', 'w') as output:
                output.write(def_content)
        else:
            with open(get_resource_path(fname), 'w') as output:
                output.write(def_content)
        return def_content

def save_file(
    fname: str,
    content: str,
    fdest: str ='relative', 
    mode: str = 'w'):
    """
    fname = filename, content = what to save to the file, 
    fdest = where to save file, mode = w for write or a for append
    import os
    """
    home = os.path.expanduser("~")
    if fdest == 'home' or fdest == 'Home':
        with open(f'{home}/{fname}', mode) as output:
            output.write(content)
    else:
        with open(get_resource_path(fname), mode) as output:
            output.write(content)

def save_file_list(
    fname: str,
    content: str,
    fdest: str ='relative'
    ):
    home = os.path.expanduser("~")
    if fdest == 'home' or fdest == 'Home':
        with open(f'{home}/{fname}', 'w') as output:
            output.write(''.join(content))
    else:
        with open(get_resource_path(fname), 'w') as output:
            output.write(''.join(content))

def save_json(
    fname: str,
    content: str,
    fdest: str = 'relative'
    ):
    home = os.path.expanduser("~")
    if fdest == 'home' or fdest == 'Home':
        with open(f'{home}/{fname}', 'w') as output:
            json.dump(content,output, sort_keys=True, indent=4)
    else:
        with open(get_resource_path(fname), 'w') as output:
            json.dump(content,output, sort_keys=True, indent=4)
                
def open_json(
    fname: str,
    fdest: str = 'relative',
    def_content: json = {'key': 'value'},
    ):
    """
    fname = filename, fdest = file destination, 
    def_content = default value if the file doesn't exist
    opens the file if it exists and returns the contents
    if it doesn't exitst it creates it writes 
    the def_content value to it and returns the def_content value
    import os, json
    """
    home = os.path.expanduser("~")
    try:
        if fdest == 'home' or fdest == 'Home':
            with open(f'{home}/{fname}', 'r') as fle:
                    content = json.load(fle)
            return content
        else:
            with open(get_resource_path(fname), 'r') as fle:
                    content = json.load(fle)
            return content
    except(FileNotFoundError, EOFError) as e:
        print(e)
        if fdest == 'home' or fdest == 'Home':
            with open(f'{home}/{fname}', 'w') as output:
                json.dump(def_content, output, sort_keys=True, indent=4)
        else:
            with open(get_resource_path(fname), 'w') as output:
                json.dump(def_content, output, sort_keys=True, indent=4)
        return def_content

def save_yaml(
    fname: str,
    dict_file: dict,
    fdest: str ='relative'
    ):
    home = os.path.expanduser("~")
    if fdest == 'home' or fdest == 'Home':
        with open(f'{home}/{fname}', 'w') as output:
            yaml.dump(dict_file,output, sort_keys=True)
    else:
        with open(get_resource_path(fname), 'w') as output:
            yaml.dump(dict_file,output, sort_keys=True)

def open_yaml(
    fname: str,
    fdest: str ='relative',
    def_content: dict = {'key': 'value'}
    ):
    """
    fname = filename, fdest = file destination, 
    def_content = default value if the file doesn't exist
    opens the file if it exists and returns the contents
    if it doesn't exitst it creates it writes 
    the def_content value to it and returns the def_content value
    import os, yaml(pip install pyyaml)
    """
    home = os.path.expanduser("~")
    try:
        if fdest == 'home' or fdest == 'Home':
            with open(f'{home}/{fname}', 'r') as fle:
                    content = yaml.full_load(fle)
            return content
        else:
            with open(get_resource_path(fname), 'r') as fle:
                    content = yaml.full_load(fle)
            return content
    except(FileNotFoundError, EOFError) as e:
        print(e)
        if fdest == 'home' or fdest == 'Home':
            with open(f'{home}/{fname}', 'w') as output:
                yaml.dump(def_content,output, sort_keys=True)
        else:
            with open(get_resource_path(fname), 'w') as output:
                yaml.dump(def_content,output, sort_keys=True)
        return def_content
        
              
# Gleen info ////////////////////////////////////////////////////
def html_info(tag,url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        find_status = soup.find(tag)
        final_status = find_status.text.strip()
    except requests.exceptions.RequestException as e:
        print(e)
        final_status = "Can't connect"
        print(final_status)
    return final_status

def list_of_items(item,range_num: int):
        """
        Not used?
        """
        items = []
        for i in range(range_num):
            temp = item
            items.append(temp)
        return items

def add_to_list(list_in,list_out):
    # takes a list of items
  for i in range(len(list_in)):
    list_out.append(list_in[i])
  return list_out

def dict_to_list(dictionary: dict):
  """
   Convert dictionary to a list
  """
  temp = []
  list_name = []
  for key, value in dictionary.items():
    temp = [key,value]
    list_name.append(temp)
  return list_name.sort()

def combine_dict(dict_list: dict):
  """
  Takes a list of dictionaries and combines into one dictionary
  requires from collections import ChainMap and python 3.3 or later
  """
  combined_dict = dict(ChainMap(*dict_list))
  return combined_dict

def group_list(
  lname: list, 
  positions: int, 
  start: int = 0
  ):
  """
  takes a list and groups them into 
  sub lists in the amount of positions
  """
  while start <= len(lname) - positions:
    yield lname[start:start + positions]
    start += positions

def random_list(lname: list):
  """
  Randomizes a list
  """
  for item in range(1):
    rand = random.sample(lname, len(lname))
  return rand

def reverse_sublist(lname: list):
  for i in range(0,len(lname),2):
    lname[i][:] = lname[i][::-1]
  return lname
    
def last_n_lines(
  fname: str, 
  lines: int, 
  fdest: str ='relative'
  ):
  """
  Gets the last so many lines of a file 
  and returns those lines in text.
  Arguments = filename, number of lines,
  file destination
  """
  home = os.path.expanduser("~")
  try:
    file_lines = []
    if fdest == 'home' or fdest == 'Home':
      with open(f'{home}/{fname}') as file:
        for line in (file.readlines() [-lines:]):
          file_lines.append(line)
    else:
      with open(get_resource_path(fname), 'r') as file:
        for line in (file.readlines() [-lines:]):
          file_lines.append(line)
    file_lines_text = (''.join(file_lines))
    return file_lines_text
  except(FileNotFoundError) as e:
    print(e)
    return 'file not found'

# Date/Time//////////////////////////////////////////////
def day_diff(
  month: int,
  day:int,
  year: int
  ):
    current = date.today()
    day = date(year,month,day)
    till_day = day - current
    return till_day.days
    
def year_current():
    current = date.today()
    current_year = current.year
    return current_year
    
def time_now() -> str:
    current =  datetime.now().strftime('%H:%M:%S')
    return current

def from_str_time_meridiem(
    str_time:str, 
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
    Requires from datetime import datetime, date, time import pytz
    '''
    if utc:
      tz =pytz.timezone('UTC')
    else:
        tz = pytz.timezone(tzone)
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
        Requires from datetime import datetime, date, time import pytz
    """
    if utc:
      tz =pytz.timezone('UTC')
    else:
        tz = pytz.timezone(tzone)

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
        Requires from datetime import datetime, date, time import pytz
    """
    if utc:
      tz =pytz.timezone('UTC')
    else:
        tz = pytz.timezone(tzone)
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

# Tempature info

def import_temp(fname: str = 'temp.txt'):
    '''
    Import temp from text file then split off each word. 
    returns current temp  
    '''
    tempin = open_file(fname)
    templist = tempin.split()
    temp, day, hour = templist
    now_hour = datetime.datetime.now().strftime('%H.%M')
    temp_diff = round(float(now_hour) - float(hour))
        
    if temp_diff == 0:  
        if temp > '0':
            print(f'Temp diff: {temp_diff}')
            print(f'This is the temp: {temp}')
            current_temp = temp
        else:
                current_temp = 'Bad Reading'
    else:
        current_temp = 'Sensor Needs Reset'
        print('Sensor needs reset')
        
    return current_temp
        
def try_float(temp: str):
    '''
    Try's to change a string into a float. 
    if it fails it returns original temp
    if it converts it returns the temp as a float
    '''
    try:
        temp = float(temp)
    except Exception as e:
        print(e)
        temp = temp
    return temp
    
# file information
def check_file_age(
  fname: str, 
  fdest: str='relative'
  ):
  """
  Returns the difference of the current timestamp and the
  timestamp of a file last write in hours 
  Arguments = filename from home dir
  Requires import os
  """
  home = os.path.expanduser("~")
  if fdest == 'home' or fdest == 'Home':
    file_info= os.stat(f'{home}/{fname}')
  else:
    file_info= os.stat(get_resource_path(fname))
  now = datetime.now().timestamp()
  modified = int(file_info.st_mtime)
  difference_hour = int(((now - modified)/60)/60)
  return difference_hour

print(from_str_date('2021-04-15', True, True))


