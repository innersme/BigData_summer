#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 09:41:43 2017

@author: innersme
"""
"""
소수 판별 함수 작성
판별 => 소수이다 or 소수가 아니다. flag = True or False
 
 - 이름 결정: isPrimeNumber
 - 파라메터 결정: 하나의 수
 - 리턴형식 결정: bool

"""


def isPrimeNumber(number):
    flag = False
    check = 0
    for i in range(1,number+1):
        if number%i==0:
            check = check + 1
    print(check)
    if check == 2:
        flag = True
    
    return flag

#