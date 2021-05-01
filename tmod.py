#! /usr/bin/env python3

# -*- coding: utf-8 -*-
version = '2021-05-01'

# Imports included with python
import random
import os
import os.path
import sys
from datetime import datetime, date, time
from smtplib import SMTP
from collections import ChainMap # Requires python 3.3
from re import search
import json

# Imports installed through pip
try:
  # pip install pyyaml if needed
  import yaml
except:
  pass

try:
  # pip install cryptography if needed
  from cryptography.fernet import Fernet
except:
  pass

# colors 
def colors():
  return {
  'PURPLE' : '\033[95m',
  'CYAN' : '\033[96m',
  'DARKCYAN' : '\033[36m',
  'BLUE'  : '\033[94m',
  'GREEN' : '\033[92m',
  'YELLOW' : '\033[93m',
  'RED' : '\033[91m',
  'BOLD' : '\033[1m',
  'UNDERLINE' : '\033[4m',
  'END' : '\033[0m'
  }

# File I/O /////////////////////////////////////////
def home_dir():
  home = os.path.expanduser('~')
  return home

def get_resource_path(rel_path):
    dir_of_py_file = os.path.dirname(sys.argv[0])
    rel_path_to_resource = os.path.join(dir_of_py_file, rel_path)
    abs_path_to_resource = os.path.abspath(rel_path_to_resource)
    return abs_path_to_resource

def open_file(
    fname: str,
    fdest: str = 'relative', 
    def_content: str = '0',
    mode: str = 'r'
    ):
    """
    fname = filename, fdest = file destination, 
    def_content = default value if the file doesn't exist,
    mode = defines read mode 'r' or 'rb'
    Opens the file if it exists and returns the contents.
    If it doesn't exitst it creates it. Writes 
    the def_content value to it and returns the def_content value
    import os
    """
    home = home_dir()
    try:
        if fdest == 'home' or fdest == 'Home':
            with open(f'{home}/{fname}', mode) as path_text:
                content=path_text.read()
        else:
            with open(get_resource_path(fname), mode) as text:
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
    home = home_dir()
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
    home = home_dir()
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
    home = home_dir()
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
    requires: import os, yaml
    """
    home = home_dir()
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
    content: dict,
    fdest: str ='relative',
    mode: str = 'w'
    ):
    """
    fname = filename, content = data to save, fdest = file destination,
    mode = 'w' for overwrite file or 'a' to append to the file
    Takes a dictionary and writes it to file specified. it will either
    write or append to the file depending on the mode method
    requires: import os, yaml
    """
    home = home_dir()
    if fdest == 'home' or fdest == 'Home':
        with open(f'{home}/{fname}', mode) as output:
            yaml.safe_dump(content,output, sort_keys=True)
    else:
        with open(get_resource_path(fname), mode) as output:
            yaml.safe_dump(content,output, sort_keys=True)

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
    home = home_dir()
    try:
        if fdest == 'home' or fdest == 'Home':
            with open(f'{home}/{fname}', 'r') as fle:
                    content = yaml.safe_load(fle)
            return content
        else:
            with open(get_resource_path(fname), 'r') as fle:
                    content = yaml.safe_load(fle)
            return content
    except(FileNotFoundError, EOFError) as e:
        print(e)
        if fdest == 'home' or fdest == 'Home':
            with open(f'{home}/{fname}', 'w') as output:
                yaml.safe_dump(def_content,output, sort_keys=True)
        else:
            with open(get_resource_path(fname), 'w') as output:
                yaml.safe_dump(def_content,output, sort_keys=True)
        return def_content
  
def check_dir(
  dname: str, 
  ddest: str = 'home'
  ):
  """
  dname = name of the file or folder,
  ddest = the destination, either home or relative to CWD
  check to see if specified dir exists.
  Requires import os
  """
  home = home_dir()
  if ddest == 'home' or ddest == 'Home':
    dpath = f'{home}/{dname}'
  else:
    dpath = get_resource_path(dname)
  dir_exist = os.path.isdir(dpath)
  return dir_exist

def make_dir(
  dname:str, 
  ddest: str = 'home'
  ):
  """
  dname = name of the file or folder,
  ddest = the destination, either home or relative to CWD
  Makes the dir specified.
  Requires import os
  """
  home = home_dir()
  if ddest == 'home' or ddest == 'Home':
    os.mkdir(f'{home}/{dname}')
  else:
    os.mkdir(get_resource_path(dname))


def remove_file(
  fname:str, 
  fdest: str = 'home'
  ):
  """
  fname = name of the file or folder,
  fdest = the destination, either home or relative to CWD
  Removes the file specified
  Requires import os
  """
  home = home_dir()
  if fdest == 'home' or fdest == 'Home':
    os.remove(f'{home}/{fname}')
  else:
    os.remove(get_resource_path(fname))

def check_file_dir(
  fname: str, 
  fdest: str = 'home'
  ):
  """
  fname = name of the file or folder,
  fdest = the destination, either home or relative to CWD
  Check if file or folder exist returns True or False
  Requires import os
  """
  home = home_dir()
  if fdest == 'home' or fdest == 'Home':
    fpath = f'{home}/{fname}'
  else:
    fpath = get_resource_path(fname)
  file_exist = os.path.exists(fpath)
  return file_exist
      
              
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
  home = home_dir()
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

# Encryption

def gen_key(fname: str,):
  home = home_dir()
  key = Fernet.generate_key()
  with open(f'{home}/{fname}', 'wb')as fkey:
    fkey.write(key)

def decrypt(
  key: str, 
  fname: str, 
  e_fname: str,
  fdest: str = 'relative'
  ):
  """
  key = key file used to encrypt file,
  fname = file to encrypt,
  e_fname = name of the encrypted file,
  fdest = file destination relative too,
  Takes a encrypted input file and dencrypts output file
  requires the tmod open_file and save_file functions
  requires from cryptography.fernet import Fernet
  """
  keyf = Fernet(key)
  encrypted = open_file(
    fname = e_fname,
    fdest = fdest, 
    mode ="rb") 
  decrypt_file = keyf.decrypt(encrypted)
  save_file(
    fname = fname,
    content = decrypt_file,
    fdest = fdest,
    mode = "wb")

def encrypt(
  key: str, 
  fname: str, 
  e_fname: str, 
  fdest='relative', 
  ):
  """
  key = key file used to encrypt file,
  fname = file to encrypt,
  e_fname = name of the encrypted file,
  fdest = file destination relative too,
  Takes a input file and encrypts output file
  requires tmod open_file and save_file functions
  requires from cryptography.fernet import Fernet
  """
  keyf = Fernet(key)
  e_file = open_file(
    fname = fname,
    fdest = fdest,
    mode = "rb"
    )
  encrypted_file = keyf.encrypt(e_file)
  save_file(
    fname = e_fname,
    content = encrypted_file,
    fdest = fdest,
    mode = "wb"
  )

def decrypt_login(
  key: str, 
  e_fname: str,
  fdest: str = 'relative'
  ):
  keyf = Fernet(key)
  encrypted = open_file(
    fname = e_fname,
    fdest = fdest,
    mode = "rb"
    )
  decrypt_file = keyf.decrypt(encrypted)
  usr = decrypt_file.decode().split(':')
  return [usr[0],usr[1]]


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


def login_info(
  fname: str, 
  fdest: str = 'home'
  ):
  """
  fname = filename of the file that has the login,
  fdest = The destination of the file
  Get login info from a yaml file
  """
  ps = open_yaml(fname, fdest)
  for key, value in ps.items():
    us = key
    psw = value
  return [us,psw]

def mail(
  body: str, 
  subject: str,
  send_to: list,
  login: list
  ):
  """
  body = Body of the message, subject = The subject,
  send_to = Who you want to send the message to,
  login = The login information for email.
  Requires from smtplib import SMTP
  """
  us, psw = login
  message = f'Subject: {subject}\n\n{body}'
  print(message)
  try:
    mail = SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.ehlo()
    mail.login(us, psw)
    mail.sendmail(us,send_to, message)
    mail.close()
    print('Successfully sent email')
  except Exception as e:
    print('Could not send email because')
    print(e)

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
  home = home_dir()
  if fdest == 'home' or fdest == 'Home':
    file_info= os.stat(f'{home}/{fname}')
  else:
    file_info= os.stat(get_resource_path(fname))
  now = datetime.now().timestamp()
  modified = int(file_info.st_mtime)
  difference_hour = int(((now - modified)/60)/60)
  return difference_hour

# colors 
def colors():
  return {
  'PURPLE' : '\033[95m',
  'CYAN' : '\033[96m',
  'DARKCYAN' : '\033[36m',
  'BLUE'  : '\033[94m',
  'GREEN' : '\033[92m',
  'YELLOW' : '\033[93m',
  'RED' : '\033[91m',
  'BOLD' : '\033[1m',
  'UNDERLINE' : '\033[4m',
  'END' : '\033[0m',
  } 
def prRedMulti(ntext,text): print(f"{ntext}\033[91m \033[1m{text}\033[00m")
def prCyanMulti(ntext,text): print(f"{ntext}\033[96m {text}\033[00m")
def prCyanMultiB(ntext,text): print(f"{ntext}\033[96m \033[1m{text}\033[00m")

def prRedBold(text): print(f"\033[91m \033[1m{text}\033[00m")
def prGreenBold(text): print(f"\033[92m \033[1m{text}\033[00m")
def prYellowBold(text): print(f"\033[93m \033[1m{text}\033[00m")
def prLightPurpleBold(text): print(f"\033[94m \033[1m{text}\033[00m")
def prPurpleBold(text): print(f"\033[95m \033[1m{text}\033[00m")
def prCyanBold(text): print(f"\033[96m \033[1m{text}\033[00m")
def prLightGrayBold(text): print(f"\033[97m \033[1m{text}\033[00m")
def prBlackBold(text): print(f"\033[98m \033[1m{text}\033[00m")

def prRed(text): print(f"\033[91m {text}\033[00m")
def prGreen(text): print(f"\033[92m {text}\033[00m")
def prYellow(text): print(f"\033[93m {text}\033[00m")
def prLightPurple(text): print(f"\033[94m {text}\033[00m")
def prPurple(text): print(f"\033[95m {text}\033[00m")
def prCyan(text): print(f"\033[96m {text}\033[00m")
def prLightGray(text): print(f"\033[97m {text}\033[00m")
def prBlack(text): print(f"\033[98m {text}\033[00m")

# Input functions
def input_list(
  subject: str, 
  description: str,
  in_type: str = 'email',
  outword: str = 'next'
  ):
  """
  subject = The subject of the input item,
  description = the description of the input item,
  in_type = tthe type of input field. Choices are 
  email, file, int, time, password
  outward = This is the word used to present to the user
  to stop adding more items.
  This would be used for a input item that you would
  want to add to a list.
  Requires: doesn't require any special imports
  """
  c = colors()
  print(
    f'\n{c["PURPLE"]}{c["BOLD"]}'
    f'{subject.capitalize()}{c["END"]}\n'
    f'You can add as many items as you like.\n'
    f'But you must add at least 1 item.\n'
    f'When your done adding, Type ' 
    f'{c["RED"]}{c["BOLD"]}{outword}{c["END"]}\n'
  )
  item_list = []
  while True:
    item: str = input(f"Enter the {subject} {description}: ")
    while (validate_input(item, in_type) == False):
      if ((
        item == outword or 
        item == outword.capitalize() or 
        item == outword.upper()) and 
        len(item_list) != 0
      ):
        break
      if item == outword or item == outword.capitalize() or item == outword.upper():
        print(
          f'{c["RED"]}{c["BOLD"]}You need to enter at least 1 ' 
          f'{in_type}{c["END"]}')
      else:
        print(
          f'{c["RED"]}{c["BOLD"]}This is not a valid ' 
          f'{in_type}{c["END"]}')
      item: str = input(f"Enter the {subject} {description}: ")
    if ((
      item == outword or 
      item == outword.capitalize() or 
      item == outword.upper()) and
      len(item_list) != 0
      ):
      length = len(item_list)
      print(
        f'\nYou have added {length} item(s), ' 
        f'Because you typed {c["RED"]}{c["BOLD"]}{item}{c["END"]}\n'
        f'That will complete your selection for "{subject.capitalize()}".')
      break
    else:
      print(f'You added {c["CYAN"]}{item}{c["END"]}')
      item_list.append(item)
    print(f'{c["CYAN"]}{item_list}{c["END"]}')
  return item_list

def input_single(
  in_message: str,
  in_type: str ='email',
  fdest: str = 'home',
  max_number: int = 200
  ):
  """
  in_message = the message you want in your input string,
  in_type = the type of input field. Choices are 
  email, file, int, time, password
  This is for a single item input. This uses "validate_input"
  to verify that items entered meet requirements for that type of input
  """
  c = colors()
  if in_type == 'int' or in_type == 'float':
    item = input(f'{in_message}(Max {max_number}): ')
  else:
   item = input(f'{in_message}: ')
  while (validate_input(
    item = item, 
    in_type = in_type,
    fdest = fdest,
    max_number = max_number
    ) == False):
    print(
      f'{c["RED"]}{c["BOLD"]}'
      f'This is not a valid {in_type}{c["END"]}')
    if in_type == 'int' or in_type == 'float':
      item = input(f'{in_message}(max {max_number}): ')
    else:
      item = input(f'{in_message}: ')
  if in_type == 'password':
    print(f'{c["CYAN"]}******{c["END"]}')
  else:
    print(f'You entered {c["CYAN"]}{item}{c["END"]}')
  if in_type == 'int':
    return int(item)
  elif in_type == 'float':
    return float(item)
  else:
    return item

def validate_input(
  item:str,
  in_type: str,
  fdest: str = 'home',
  max_number: int = 200 
  ):
  """
  item = The data entered in the input field,
  email, file, password, int, float, time
  in_type = The type of data it is suposed to be,
  max_number = the max number that can be ablied this if for int only.
  Takes the input and checks to see if it is 
  valid for its data type.
  """
  if in_type == 'email':
    print(item)
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if (search(regex,item)):
      return True
    else:
      return False
  elif in_type == 'file':
    if not item:
      return False
    else:
     return check_file_dir(item, fdest)
  elif in_type == 'password':
    if not item:
      return False
  elif in_type == 'time':
    try:
      datetime.strptime(item,'%H:%M').time()
      return True
    except ValueError:
      return False
  elif in_type == 'int':
    try:
      number = int(item)
      if (number <=0) or (number > max_number):
        return False
      return True
    except Exception:
      return False
  elif in_type == 'float':
    try:
      number = float(item)
      if (number <=0) or (number > max_number):
        return False
      return True
    except Exception:
      return False
  else:
    return False

## Wizard setup
def config_setup(conf_dir: str):
  """
  conf_dir = Configuration dir. This would 
  normally be in the .config/progName,
  This commandline wizard creates the 
  program config dir and populates the 
  setup configuration file. Sets up username 
  and password for email notifications
  """
  c = colors()
  home = home_dir()
  make_dir(conf_dir)

  print(
    f'\n{c["YELLOW"]}{c["BOLD"]}We could not find any ' 
    f'configuration folder{c["END"]}'
    f'\n{c["GREEN"]}This Wizard will ask some questions ' 
    f'to setup the configuration needed for the script to function.{c["END"]}'
    f'\n{c["GREEN"]}{c["BOLD"]}This configuration wizard will only run once.{c["END"]}\n'
    f'\n{c["GREEN"]}The first 2 questions are going ' 
    f'to be about your email and password you are using to send. '
    f'\nThis login information will be stored on your local ' 
    f'computer encrypted seperate '
    f'\nfrom the rest of the configuration. ' 
    f'This is not viewable by browsing the filesystem{c["END"]}'
  )

  gen_key(f'{conf_dir}/.info.key')
  key = open_file(
      fname = f'{conf_dir}/.info.key', 
      fdest = "home",
      mode ="rb"
      )
  prYellowBold(no_config)
  prGreen(intr_desc1)
  prGreenBold(intr_desc2)
  prGreen(intr_desc3)

  email = input_single(
    in_message = "\nEnter your email",
    in_type = 'email'
   )
  pas = input_single(
    in_message = "\nEnter your password",
    in_type = 'password')
  lo = {email:pas}
  save_yaml(
    fname = f'{conf_dir}/.cred.yaml',
    fdest = 'home',
    content = lo
    )
  encrypt(
    key = key,
    fname = f'{conf_dir}/.cred.yaml',
    e_fname = f'{conf_dir}/.cred_en.yaml',
    fdest = 'home'
    )
  remove_file(f'{conf_dir}/.cred.yaml')
  run = input_single(
    in_message ="Enter the time to run the script daily(Example: 05:00)",
    in_type = "time"
    )
  numb_lines = input_single(
    in_message='Enter the number of lines from the end of log file to send',
    in_type = 'int',
    max_number = 400
    )
  send_list = input_list(
    subject= "email address",
    description = 'to send to (example@gmail.com)',
    in_type = 'email')
  log_list = input_list(
    subject= "log file",
    description = 'to check relative to your home dir (Example: Logs/net_backup.log)',
    in_type = 'file'
    )
  load = {
    'runtime': run,
    'lines': int(numb_lines),
    'sendto': send_list,
    'logs': log_list
    }
  save_yaml(
    fname =f'{conf_dir}/emailog_set.yaml',
    fdest = 'home',
    content = load)
  print(
    f'\n{c["YELLOW"]}{c["BOLD"]}This completes the wizard{c["END"]}'
    f'\nThe configuration file has been written to disk'
    f'\nIf you want to change the settings you can edit ' 
    f'{c["CYAN"]}{c["BOLD"]}{home}/{conf_dir}/emailog_set.yaml{c["END"]}'
    f'\n{c["GREEN"]}{c["BOLD"]}This wizard ' 
    f'won\'t run any more, So the script can ' 
    f'now be run automatically{c["END"]}\n'
    f'\n{c["CYAN"]}{c["BOLD"]}You can stop ' 
    f'the script by typing Ctrl + C{c["END"]}\n')

