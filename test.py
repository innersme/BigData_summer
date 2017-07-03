#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 16:02:51 2017

@author: innersme
"""
import baseball

targetNumber = baseball.makeNumber(3)

while True:
    guessNumber = 0
    while True:
        #임의의 숫자 입력
        guessNumber = input('자릿수를 입력하세요 >>> ')
        #
        check = baseball.isSameNumber(guessNumber)
        #isSameNumber가 not(False)=True 라면,
        if not check:
            break
        #isSameNumber가 False라면, 중복발생.
        else:
            print("중복발생")

    result = baseball.compareNumber(targetNumber,guessNumber)
    if result[0] == 3:
        print('정답입니다.')
        break
    else :
        print("%d strike(s), %d ball(s)"%(result[0],result[1]))
        