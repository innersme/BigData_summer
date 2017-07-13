# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 14:11:56 2017

@author: user
"""
#py파일명으로 import가 필요하다.
import week2_tue_mycal

# input은 입력을 string형태로 받는다.
month = input("월 입력 >>")
year = input("년도 입력 >>")
# int로 형 변환이 필요하다.
viewMonth(int(year), int(month))
