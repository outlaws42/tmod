#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Functions dealing with lists and dictionaries
"""



__author__ = "Troy Franks"
__version__ = "2023-03-23"


ddef add_to_list(
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
