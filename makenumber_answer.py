#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 15:04:31 2017

@author: innersme

1. 사용자로부터 입력
2. 중복제거 로직
 - 각 자리수가 다른 자릿수의 수와 같은지 비교
3. 관리 로직 흐름

"""

"""
        if check:
            continue
        else: break

==

        if not check:
            break
            
같은 로직 ?

"""    
import random

#숫자 만들기 string number로 출력
def makeNumber(num):
    #random으로 number를 생성했다.
    number = str(int(random.random()*(10**num-10**(num-1)))+10**(num-1))
    while True:
        check = isSameNumber(number)
        if not check:
            break
    return str(number)

#같은 숫자가 있는지 없는지 확인.
def isSameNumber(strNumber): #string number를 받는다.
    flag = False #flag기법
    # 각각의 string number를 검사
    for item in strNumber:
        # 만약 입력받은 변수안에 item이 있다면
        if item in strNumber:
            flag = True
            break
    print("flag %s"%flag)
    return flag

# 비교로직
def compareNumber(targetNumber,guessNumber):
    strike = 0
    ball = 0
    #처리 로직
    return strike

# ---------------------------------------------
targetNumber = makeNumber(3) # string Number 

while True:
    guessNumber = 0
    while True:
        seed = input("자릿수를 입력하세요 >>> ")
        check = isSameNumber(seed)
        if not check:
            break
    """판별로직 호출""" 
    result = compareNumber(targetNumber, guessNumber)
        
    """결과처리"""
    if result == 3:
        print("correct")
        break
    else: 
        print("try again")




