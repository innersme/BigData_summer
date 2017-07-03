#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 16:02:20 2017

@author: innersme
"""
import random
#stringtype Number 입력받는데, 출력값은 flag
#숫자가 같니 isSameNumber?
def isSameNumber(strNumber):
    #같지 않다(초기값)
    flag = False
    #i [0,1,2,...,len(strNumber)-1]
    for i in range(len(strNumber)-1):
        #
        for j in range(i+1,len(strNumber)):
            if strNumber[i] == strNumber[j]:
                flag = True
                break
    return flag

#숫자 만들기 (num)
def makeNumber(num):
    #계속 반복한다. 무엇을? 
    #몇번 반복하는지 몰라 -> while사용
    while True:
        #입력받은 num자리수 예를들어 makeNumber(2) = 10 - 99 (string type)
        number = int(random.random()*(10**num-10**(num-1)))+10**(num-1)
        #작업이 다르면 서로 분리해
        check = isSameNumber(str(number))
        #중복되었니? not False = True 
        #check 
        if not check:
            break
            
    #return number 값.string type
    return str(number)    

def compareNumber(targetNumber,guessNumber):
    strike = 0
    ball = 0
    for j in range(len(targetNumber)):
        for i in range(len(guessNumber)):
            if targetNumber[j]==guessNumber[i] and i==j:
                strike = strike + 1
            elif targetNumber[j]==guessNumber[i] and i!=j:
                ball = ball + 1
    #처리 로직
    #return [strike, ball] 과 같이 return 값을 list로 출력할 수 있다. 
    #result[0], result[1] 이런식으로 출력하면 됨!
    return [strike,ball]
