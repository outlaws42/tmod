#! /usr/bin/env python3

# -*- coding: utf-8 -*-

"""
Functions to work with doing a wizard to setup configuration files.
"""

# Standard Library Imports
from datetime import datetime, date

# Imports from tmods


__author__ = "Troy Franks"
__version__ = "2023-03-30"


def day_diff(
    month: int,
    day: int,
    year: int,
):
    """
    Takes a date month, day, year. Outputs the
    difference between that date and todays date
    Requires from datetime import date
    """
    current = date.today()
    day_target = date(year, month, day)
    till_day = day_target - current
    return till_day.days


def year_current():
    current = date.today()
    current_year = current.year
    return current_year


def time_now() -> str:
    current = datetime.now().strftime("%H:%M:%S")
    return current


diff = day_diff(month=12, day=25, year=2023)
print(diff)
