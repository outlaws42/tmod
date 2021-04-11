#! /usr/bin/env python3

# -*- coding: utf-8 -*-
version = '2021-04-11'

# Imports included with python
import random
import os
import os.path
import sys
from datetime import datetime, date
from collections import ChainMap # Requires python 3.3
import json

# Imports installed through pip
try:
  # pip install pyyaml if needed
  import yaml
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

def open_file(file_,type_='relative'):
    home = os.path.expanduser("~")
    try:
        if type_ == 'home' or type_ == 'Home':
            with open(f'{home}/{file_}', 'r') as path_text:
                variable=path_text.read()
        else:
            with open(get_resource_path(file_), 'r') as text:
                variable=text.read()
        return variable
    except(FileNotFoundError) as e:
        print(e)
        print('It is reading here')
        variable = '0'
        if type_ == 'home' or type_ == 'Home':
            with open(f'{home}/{file_}', 'w') as output:
                output.write(variable)
        else:
            with open(get_resource_path(file_), 'w') as output:
                output.write(variable)

def save_file(file_,variable,type_='relative'):
    home = os.path.expanduser("~")
    if type_ == 'home' or type_ == 'Home':
        with open(f'{home}/{file_}', 'w') as output:
            output.write(variable)
    else:
        with open(get_resource_path(file_), 'w') as output:
            output.write(variable)

def save_file_list(file_,variable,type_='relative'):
    home = os.path.expanduser("~")
    if type_ == 'home' or type_ == 'Home':
        with open(f'{home}/{file_}', 'w') as output:
            output.write(''.join(variable))
    else:
        with open(get_resource_path(file_), 'w') as output:
            output.write(''.join(variable))

def save_file_append(file_,variable,type_='relative'):
    home = os.path.expanduser("~")
    if type_ == 'home' or type_ == 'Home':
        with open(f'{home}/{file_}', 'a') as output:
            output.write(variable)
    else:
        with open(get_resource_path(file_), 'a') as output:
            output.write(variable)

def save_json(file_,variable,type_='relative'):
    home = os.path.expanduser("~")
    if type_ == 'home' or type_ == 'Home':
        with open(f'{home}/{file_}', 'w') as output:
            json.dump(variable,output, sort_keys=True, indent=4)
    else:
        with open(get_resource_path(file_), 'w') as output:
            json.dump(variable,output, sort_keys=True, indent=4)
                
def open_json(file_,type_='relative'):
    home = os.path.expanduser("~")
    try:
        if type_ == 'home' or type_ == 'Home':
            with open(f'{home}/{file_}', 'r') as fle:
                    variable = json.load(fle)
            return variable
        else:
            with open(get_resource_path(file_), 'r') as fle:
                    variable = json.load(fle)
            return variable
    except(FileNotFoundError, EOFError) as e:
        print(e)
        variable = 0
        if type_ == 'home' or type_ == 'Home':
            with open(f'{home}/{file_}', 'w') as fle:
                json.dump(variable, fle)
        else:
            with open(get_resource_path(file_), 'w') as fle:
                json.dump(variable, fle)

def save_yaml(file_,dict_file,type_='relative'):
    home = os.path.expanduser("~")
    if type_ == 'home' or type_ == 'Home':
        with open(f'{home}/{file_}', 'w') as output:
            yaml.dump(dict_file,output, sort_keys=True)
    else:
        with open(get_resource_path(file_), 'w') as output:
            yaml.dump(dict_file,output, sort_keys=True)

def open_yaml(file_,type_='relative'):
    home = os.path.expanduser("~")
    try:
        if type_ == 'home' or type_ == 'Home':
            with open(f'{home}/{file_}', 'r') as fle:
                    variable = yaml.full_load(fle)
            return variable
        else:
            with open(get_resource_path(file_), 'r') as fle:
                    variable = yaml.full_load(fle)
            return variable
    except(FileNotFoundError, EOFError) as e:
        print(e)
        variable = 0
        if type_ == 'home' or type_ == 'Home':
            with open(f'{home}/{file_}', 'w') as fle:
                yaml.dump(variable, fle)
        else:
            with open(get_resource_path(file_), 'w') as fle:
                yaml.dump(variable, fle)
              
def open_log_file(file_,type_='home'):
    home = os.path.expanduser("~")
    try:
        if type_ == 'home' or type_ == 'Home':
            with open(f'{home}/Logs/{file_}', 'r') as path_text:
                variable=path_text.read()
        else:
            with open(get_resource_path(file_), 'r') as text:
                variable=text.read()
        return variable
    except(FileNotFoundError) as e:
        print(e)
        print('It is reading here')
        variable = '0'
        if type_ == 'home' or type_ == 'Home':
            with open(f'{home}/{file_}', 'w') as output:
                output.write(variable)
        else:
            with open(get_resource_path(file_), 'w') as output:
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

def dict_to_list(list_,dictionary_):
        # Convert dictionary to a list
        temp = []
        list_ = []
        for key, value in dictionary_.items():
            temp = [key,value]
            list_.append(temp)
        return list_.sort()

def combine_dict(dict_list):
        """
        Takes a list of dictionarys and combines into one dictionary
        requires from collections import ChainMap and python 3.3 or later
        """
        current = dict(ChainMap(*dict_list))
        return current

def group_list(list_, positions, start=0):
    """
    takes a list and groups them into sub list in the amount of positions
    """
    while start <= len(list_) - positions:
        yield list_[start:start + positions]
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

def timestamp_from_string_time(str_time):
    '''
    Takes a string time with AM or PM and 
    converts it to a Unix timestamp
    '''
    dt_time = datetime.strptime(str_time, '%I:%M %p').time()
    today_date = datetime.today().date()
    str_date = today_date.strftime('%Y-%m-%d')
    year, month, day = str_date.split('-')
    dt = datetime.combine(
      date(int(year), int(month), int(day)), dt_time)
    ts = int(dt.timestamp())
    return ts



def import_temp(file_='temp.txt'):
    '''
    Import temp from text file then split off each word. 
    returns current temp  
    '''
    tempin = open_file(file_)
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
