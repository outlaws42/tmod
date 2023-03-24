#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Functions dealing with html or web  stuff
"""

from bs4 import BeautifulSoup
import requests


__author__ = "Troy Franks"
__version__ = "2023-03-23"


def html_info(tag, url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        find_status = soup.find(tag)
        final_status = find_status.text.strip()
    except requests.exceptions.RequestException as e:
        print(e)
        final_status = "Can't connect"
        print(final_status)
    return final_status
