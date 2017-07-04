# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 13:36:12 2017

@author: user
module 
"""

import time
now = time.localtime()
print(now.tm_year)

import calendar
result = calendar.monthcalendar(2017,8)
print(result)
month = calendar.month(2017, 8)
print(month)

result_cal = calendar.monthrange()