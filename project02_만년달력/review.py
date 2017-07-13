#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 09:18:40 2017

@author: innersme
"""

#조건이 있을 때,
"""
for i in range(1,11):
    if i%2 == 0:
        print('%d is even'%i)
    else:
        print('%d is odd'%i)
"""

# 조건이 두 개 있을 때?

year = 2231
#and or 사용하기
if (year%4==0 and year%100!=0) or year%400==0:
    print("leap year")
else :
    print("general year")


    
