#! /usr/bin/env python3

# -*- coding: utf-8 -*-

"""
Functions to work with doing a wizard to setup configuration files.
"""

# Standard Library Imports
from datetime import date

# Imports from tmods


__author__ = "Troy Franks"
__version__ = "2023-03-30"


def day_diff(month: int, day: int, year: int):
    current = date.today()
    day = date(year, month, day)
    till_day = day - current
    return till_day.days


diff = day_diff(month=12, day=25, year=2023)
print(diff)
