#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 16:02:51 2017

@author: innersme
string도 list로 사용할 수 있다.

"""
#baseball.py import
import baseball

#target임의의 (3)자리 숫자 makeNumber
targetNumber = baseball.makeNumber(3)

#반복 
while True:
    guessNumber = 0
    while True:
        #임의의 숫자 입력
        #input함수는 출력값으로 string변수형을 가진다.
        guessNumber = input('자릿수를 입력하세요 >>> ')
        #isSameNumber가 string변수형 Number를 입력값으로 가진다.
        check = baseball.isSameNumber(guessNumber)
        #isSameNumber가 not(True)=False 라면,break = 다음으로 넘어가.
        if not check:
            break
        #isSameNumber가 not(False)= True라면, print(중복발생.)
        else:
            print("중복발생")
    
    #비교함수 result
    result = baseball.compareNumber(targetNumber,guessNumber)
    #result[0] = strike
    if result[0] == 3:
        print('정답입니다.')
        #while문 탈출
        break
    else :
        #
        print("%d strike(s), %d ball(s)"%(result[0],result[1]))
        