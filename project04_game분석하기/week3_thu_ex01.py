# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
outer_line = []
file = open('install.csv', 'r')
linses = file.readlines()
for line in lines:
    outer_line.append(list(line))
    
print(len(outer_line))