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


def prRedMulti(ntext, text):
    print(f"{ntext}\033[91m \033[1m{text}\033[00m")


def prCyanMulti(ntext, text):
    print(f"{ntext}\033[96m {text}\033[00m")


def prCyanMultiB(ntext, text):
    print(f"{ntext}\033[96m \033[1m{text}\033[00m")


def prRedBold(text):
    print(f"\033[91m \033[1m{text}\033[00m")


def prGreenBold(text):
    print(f"\033[92m \033[1m{text}\033[00m")


def prYellowBold(text):
    print(f"\033[93m \033[1m{text}\033[00m")


def prLightPurpleBold(text):
    print(f"\033[94m \033[1m{text}\033[00m")


def prPurpleBold(text):
    print(f"\033[95m \033[1m{text}\033[00m")


def prCyanBold(text):
    print(f"\033[96m \033[1m{text}\033[00m")


def prLightGrayBold(text):
    print(f"\033[97m \033[1m{text}\033[00m")


def prBlackBold(text):
    print(f"\033[98m \033[1m{text}\033[00m")


def prRed(text):
    print(f"\033[91m {text}\033[00m")


def prGreen(text):
    print(f"\033[92m {text}\033[00m")


def prYellow(text):
    print(f"\033[93m {text}\033[00m")


def prLightPurple(text):
    print(f"\033[94m {text}\033[00m")


def prPurple(text):
    print(f"\033[95m {text}\033[00m")


def prCyan(text):
    print(f"\033[96m {text}\033[00m")


def prLightGray(text):
    print(f"\033[97m {text}\033[00m")


def prBlack(text):
    print(f"\033[98m {text}\033[00m")
