#! /usr/bin/env python3

# -*- coding: utf-8 -*-

"""
This is a collection of helper scripts I created for generic repeatable
operations. This version is specific to code needed for this operation.
To find the full version look for tmod in version control.
"""

# Imports included with python
import os
import os.path
import sys
import json

# Imports installed through pip
try:
    # pip install pyyaml if needed
    import yaml
except ModuleNotFoundError:
    pass

__author__ = "Troy Franks"
__version__ = "2023-03-23"


def home_dir():
    home = os.path.expanduser("~")
    return home


def get_resource_path(rel_path):
"""
Returns absolute path from a relative path
Requires sys
"""
    dir_of_py_file = os.path.dirname(sys.argv[0])
    rel_path_to_resource = os.path.join(dir_of_py_file, rel_path)
    abs_path_to_resource = os.path.abspath(rel_path_to_resource)
    return abs_path_to_resource


def open_file(
    fname: str,
    fdest: str = "relative",
    def_content: str = "0",
    mode: str = "r",
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
        if fdest == "home" or fdest == "Home":
            with open(f"{home}/{fname}", mode) as path_text:
                content = path_text.read()
        else:
            with open(get_resource_path(fname), mode) as text:
                content = text.read()
        return content
    except FileNotFoundError as e:
        print(e)
        print("It is reading here")
        if fdest == "home" or fdest == "Home":
            with open(f"{home}/{fname}", "w") as output:
                output.write(def_content)
        else:
            with open(get_resource_path(fname), "w") as output:
                output.write(def_content)
        return def_content


def save_file(
    fname: str,
    content: str,
    fdest: str = "relative",
    mode: str = "w",
):
    """
    fname = filename, content = what to save to the file,
    fdest = where to save file, mode = w for write or a for append
    import os
    """
    home = home_dir()
    if fdest == "home" or fdest == "Home":
        with open(f"{home}/{fname}", mode) as output:
            output.write(content)
    else:
        with open(get_resource_path(fname), mode) as output:
            output.write(content)


def save_file_list(
    fname: str,
    content: str,
    fdest: str = "relative",
):
    home = home_dir()
    if fdest == "home" or fdest == "Home":
        with open(f"{home}/{fname}", "w") as output:
            output.write("".join(content))
    else:
        with open(get_resource_path(fname), "w") as output:
            output.write("".join(content))


def save_json(
    fname: str,
    content: str,
    fdest: str = "relative",
):
    """
    fname = filename, fdest = file destination,
    content = value you want to save to the file.
    requires: import os, json
    """
    home = home_dir()
    if fdest == "home" or fdest == "Home":
        with open(f"{home}/{fname}", "w") as output:
            json.dump(content, output, sort_keys=True, indent=4)
    else:
        with open(get_resource_path(fname), "w") as output:
            json.dump(content, output, sort_keys=True, indent=4)


def open_json(
    fname: str,
    fdest: str = "relative",
    def_content: json = {"key": "value"},
):
    """
    fname = filename, fdest = file destination,
    def_content = default value if the file doesn't exist
    opens the file if it exists and returns the contents
    if it doesn't exitst it creates it writes
    the def_content value to it and returns the def_content value
    requires: import os, json
    """
    home = home_dir()
    try:
        if fdest == "home" or fdest == "Home":
            with open(f"{home}/{fname}", "r") as fle:
                content = json.load(fle)
            return content
        else:
            with open(get_resource_path(fname), "r") as fle:
                content = json.load(fle)
            return content
    except (FileNotFoundError, EOFError) as e:
        print(e)
        if fdest == "home" or fdest == "Home":
            with open(f"{home}/{fname}", "w") as output:
                json.dump(def_content, output, sort_keys=True, indent=4)
        else:
            with open(get_resource_path(fname), "w") as output:
                json.dump(def_content, output, sort_keys=True, indent=4)
        return def_content


def save_yaml(
    fname: str,
    content: dict,
    fdest: str = "relative",
    mode: str = "w",
):
    """
    fname = filename, content = data to save, fdest = file destination,
    mode = 'w' for overwrite file or 'a' to append to the file
    Takes a dictionary and writes it to file specified. it will either
    write or append to the file depending on the mode method
    requires: import os, yaml
    """
    home = home_dir()
    if fdest == "home" or fdest == "Home":
        with open(f"{home}/{fname}", mode) as output:
            yaml.safe_dump(content, output, sort_keys=True)
    else:
        with open(get_resource_path(fname), mode) as output:
            yaml.safe_dump(content, output, sort_keys=True)


def open_yaml(
    fname: str,
    fdest: str = "relative",
    def_content: dict = {"key": "value"},
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
        if fdest == "home" or fdest == "Home":
            with open(f"{home}/{fname}", "r") as fle:
                content = yaml.safe_load(fle)
            return content
        else:
            with open(get_resource_path(fname), "r") as fle:
                content = yaml.safe_load(fle)
            return content
    except (FileNotFoundError, EOFError) as e:
        print(e)
        if fdest == "home" or fdest == "Home":
            with open(f"{home}/{fname}", "w") as output:
                yaml.safe_dump(def_content, output, sort_keys=True)
        else:
            with open(get_resource_path(fname), "w") as output:
                yaml.safe_dump(def_content, output, sort_keys=True)
        return def_content


def check_dir(
    dname: str,
    ddest: str = "home",
):
    """
    dname = name of the dir or folder,
    ddest = the destination, either home or relative to CWD
    check to see if specified dir exists.
    Requires import os
    """
    home = home_dir()
    if ddest == "home" or ddest == "Home":
        dpath = f"{home}/{dname}"
    else:
        dpath = get_resource_path(dname)
    dir_exist = os.path.isdir(dpath)
    return dir_exist


def make_dir(
    dname: str,
    ddest: str = "home",
):
    """
    dname = name of the file or folder,
    ddest = the destination, either home or relative to CWD
    Makes the dir specified.
    Requires import os
    """
    home = home_dir()
    if ddest == "home" or ddest == "Home":
        os.mkdir(f"{home}/{dname}")
    else:
        os.mkdir(get_resource_path(dname))


def remove_file(
    fname: str,
    fdest: str = "home",
):
    """
    fname = name of the file or folder,
    fdest = the destination, either home or relative to CWD
    Removes the file specified
    Requires import os
    """
    home = home_dir()
    if fdest == "home" or fdest == "Home":
        os.remove(f"{home}/{fname}")
    else:
        os.remove(get_resource_path(fname))


def check_file_dir(
    fname: str,
    fdest: str = "home",
):
    """
    fname = name of the file or folder,
    fdest = the destination, either home or relative to CWD
    Check if file or folder exist returns True or False
    Requires import os
    """
    home = home_dir()
    if fdest == "home" or fdest == "Home":
        fpath = f"{home}/{fname}"
    else:
        fpath = get_resource_path(fname)
    file_exist = os.path.exists(fpath)
    return file_exist


def last_n_lines(
    fname: str,
    lines: int,
    fdest: str = "relative",
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
        if fdest == "home" or fdest == "Home":
            with open(f"{home}/{fname}") as file:
                for line in file.readlines()[-lines:]:
                    file_lines.append(line)
        else:
            with open(get_resource_path(fname), "r") as file:
                for line in file.readlines()[-lines:]:
                    file_lines.append(line)
        file_lines_text = "".join(file_lines)
        return file_lines_text
    except FileNotFoundError as e:
        print(e)
        return "file not found"
