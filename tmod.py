#! /usr/bin/env python3

# -*- coding: utf-8 -*-
version = '2021-04-15'

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
    fname,
    fdest='relative', 
    variable = '0'
    ):
    home = os.path.expanduser("~")
    try:
        if fdest == 'home' or fdest == 'Home':
            with open(f'{home}/{fname}', 'r') as path_text:
                variable=path_text.read()
        else:
            with open(get_resource_path(fname), 'r') as text:
                variable=text.read()
        return variable
    except(FileNotFoundError) as e:
        print(e)
        print('It is reading here')
        if fdest == 'home' or fdest == 'Home':
            with open(f'{home}/{fname}', 'w') as output:
                output.write(variable)
        else:
            with open(get_resource_path(fname), 'w') as output:
                output.write(variable)
        return variable

def save_file(
    fname: str,
    variable: str,
    fdest: str ='relative', 
    mode: str = 'w'):
    """
    fname = filename, variable = what to save to the file, 
    fdest = where to save file, mode = w for write or a for append
    """
    home = os.path.expanduser("~")
    if fdest == 'home' or fdest == 'Home':
        with open(f'{home}/{fname}', mode) as output:
            output.write(variable)
    else:
        with open(get_resource_path(fname), mode) as output:
            output.write(variable)

def save_file_list(
    fname,
    variable,
    fdest='relative'
    ):
    home = os.path.expanduser("~")
    if fdest == 'home' or fdest == 'Home':
        with open(f'{home}/{fname}', 'w') as output:
            output.write(''.join(variable))
    else:
        with open(get_resource_path(fname), 'w') as output:
            output.write(''.join(variable))

def save_json(
    fname,
    variable,
    fdest='relative'
    ):
    home = os.path.expanduser("~")
    if fdest == 'home' or fdest == 'Home':
        with open(f'{home}/{fname}', 'w') as output:
            json.dump(variable,output, sort_keys=True, indent=4)
    else:
        with open(get_resource_path(fname), 'w') as output:
            json.dump(variable,output, sort_keys=True, indent=4)
                
def open_json(
    fname,
    fdest='relative'
    ):
    home = os.path.expanduser("~")
    try:
        if fdest == 'home' or fdest == 'Home':
            with open(f'{home}/{fname}', 'r') as fle:
                    variable = json.load(fle)
            return variable
        else:
            with open(get_resource_path(fname), 'r') as fle:
                    variable = json.load(fle)
            return variable
    except(FileNotFoundError, EOFError) as e:
        print(e)
        variable = 0
        if fdest == 'home' or fdest == 'Home':
            with open(f'{home}/{fname}', 'w') as fle:
                json.dump(variable, fle)
        else:
            with open(get_resource_path(fname), 'w') as fle:
                json.dump(variable, fle)

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
    fname,
    fdest='relative'
    ):
    home = os.path.expanduser("~")
    try:
        if fdest == 'home' or fdest == 'Home':
            with open(f'{home}/{fname}', 'r') as fle:
                    variable = yaml.full_load(fle)
            return variable
        else:
            with open(get_resource_path(fname), 'r') as fle:
                    variable = yaml.full_load(fle)
            return variable
    except(FileNotFoundError, EOFError) as e:
        print(e)
        variable = 0
        if fdest == 'home' or fdest == 'Home':
            with open(f'{home}/{fname}', 'w') as fle:
                yaml.dump(variable, fle)
        else:
            with open(get_resource_path(fname), 'w') as fle:
                yaml.dump(variable, fle)
              
def open_log_file(
    fname,
    fdest='home'
    ):
    home = os.path.expanduser("~")
    try:
        if fdest == 'home' or fdest == 'Home':
            with open(f'{home}/Logs/{fname}', 'r') as path_text:
                variable=path_text.read()
        else:
            with open(get_resource_path(fname), 'r') as text:
                variable=text.read()
        return variable
    except(FileNotFoundError) as e:
        print(e)
        print('It is reading here')
        variable = '0'
        if fdest == 'home' or fdest == 'Home':
            with open(f'{home}/{fname}', 'w') as output:
                output.write(variable)
        else:
            with open(get_resource_path(fname), 'w') as output:
                output.write(variable)

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

def list_of_items(item,range_num):
        # forecast high / low temp for 3 days    
        list_ = []
        for i in range(range_num):
            temp = item
            list_.append(temp)
        return list_

def add_to_list(list_in,list_out):
    # takes a list of items
  for i in range(len(list_in)):
    list_out.append(list_in[i])
  return list_out

def dict_to_list(dictionary):
  """
   Convert dictionary to a list
  """
  temp = []
  list_name = []
  for key, value in dictionary.items():
    temp = [key,value]
    list_name.append(temp)
  return list_name.sort()

def combine_dict(dict_list):
  """
  Takes a list of dictionaries and combines into one dictionary
  requires from collections import ChainMap and python 3.3 or later
  """
  current = dict(ChainMap(*dict_list))
  return current

def group_list(lname, positions, start=0):
  """
  takes a list and groups them into 
  sub lists in the amount of positions
  """
  while start <= len(lname) - positions:
    yield lname[start:start + positions]
    start += positions

def random_list(list_):
    """
        Randomizes a list
    """
    for item in range(1):
        rand = random.sample(list_, len(list_))
    return rand

def reverse_sublist(self,list_):
    for i in range(0,len(list_),2):
        list_[i][:] = list_[i][::-1]
    return list_
    
def last_n_lines(fname, lines, fdest='relative'):
  """
  Gets the last so many lines of a file 
  and returns those lines in text.
  Arguments = filename, number of lines
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
def day_diff(month,day,year):
    current = date.today()
    day = date(year,month,day)
    till_day = day - current
    return till_day.days
    
def year_current():
    current = date.today()
    current_year = current.year
    return current_year
    
def time_now():
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

def str_date_from_datetime(dt):
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

def import_temp(fname='temp.txt'):
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
        
def try_float(temp):
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
def check_file_age(fname, fdest='relative'):
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


