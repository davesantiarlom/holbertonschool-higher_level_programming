#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tru Jun 3 15:13:37 2022
@author: David Santiago
"""

import json
from sys import argv


"""
This file contains a function that adds
all arguments to a python list and saves
to a file
"""


save_json = __import__('7-save_to_json_file').save_to_json_file
load_json = __import__('8-load_from_json_file').load_from_json_file

filename = 'add_item.json'
        """
        Represents of Student into json format
        Attributes:
            attrs (dict): A python object to convert
        Return:
            Student class as a json format
        """
try:
    new = load_json(filename)
except (ValueError, FileNotFoundError):
    new = []
        """
        Represents of Student into json format
        Attributes:
            attrs (dict): A python object to convert
        Return:
            Student class as a json format
        """
new = new + argv[1:]
save_json(new, filename)
