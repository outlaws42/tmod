#! /usr/bin/env python3

# -*- coding: utf-8 -*-

"""
Assign colors for commandline use.
"""

__author__ = "Troy Franks"
__version__ = "2023-03-23"


def colors():
    return {
        "PURPLE": "\033[95m",
        "CYAN": "\033[96m",
        "DARKCYAN": "\033[36m",
        "BLUE": "\033[94m",
        "GREEN": "\033[92m",
        "YELLOW": "\033[93m",
        "RED": "\033[91m",
        "BOLD": "\033[1m",
        "UNDERLINE": "\033[4m",
        "END": "\033[0m",
    }
