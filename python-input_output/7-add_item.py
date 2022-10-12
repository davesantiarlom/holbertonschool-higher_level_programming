#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tru Jun 3 15:13:37 2022

@author: David Arias
"""
"""
Script that adds all arguments to a Python list, and then saves them to a file
"""

from sys import argv

'print(__import__("my_module").MyClass.__doc__)'
save_to_json_file = __import__("7-save_to_json_file").save_to_json_file
load_from_json_file = __import__("8-load_from_json_file").load_from_json_file

'print(__import__("my_module").MyClass.__doc__)'
filename = "add_item.json"

'print(__import__("my_module").MyClass.__doc__)'

try:
    json_list = load_from_json_file(filename)
except:
    json_list = []
    
'print(__import__("my_module").MyClass.__doc__)'

for arg in argv[1:]:
    json_list.append(arg)

save_to_json_file(json_list, filename)
