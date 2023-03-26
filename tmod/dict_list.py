#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Functions dealing with lists and dictionaries
"""


__author__ = "Troy Franks"
__version__ = "2023-03-23"


def add_to_list(
    list_in: list,
    list_out: list,
):
    """
    list_in = list of lists,
    list_out = list you are adding to.
    takes a list of items and
    adds it to another list
    """
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
        temp = [key, value]
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
    start: int = 0,
):
    """
    takes a list and groups them into
    sub lists in the amount of positions
    """
    while start <= len(lname) - positions:
        yield lname[start : start + positions]
        start += positions


def random_list(lname: list):
    """
    Randomizes a list
    """
    for item in range(1):
        rand = random.sample(lname, len(lname))
    return rand


def reverse_sublist(lname: list):
    for i in range(0, len(lname), 2):
        lname[i][:] = lname[i][::-1]
    return lname
