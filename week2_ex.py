#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 13:04:18 2017

@author: innersme

[야구게임작성]

중복되지 않는 3자리수를 생성한다.
중복되지 않는 임의의 3자리수를 작성한다.
생성된 수와 입력할 수를 비교하여
 - 숫자가 같고 자릿수가 틀리면 ball
 - 숫자가 같고 자릿수가 같으면 strike
비교결과가 3strike이면 종료되는 코드를 작성하시오.

"""

#num를 입력값으로 받는 
import random
a = []

#중복되지 않는 n자리수를 생성한다.
def makeNumber(num):
    for i in range(num):
        rnd = random.random()
        temp = int(rnd*10)
        if temp in a:
            continue
        a.append(temp)
    return a
    
#중복되지 않는 임의의 3자리수를 작성한다.
def inPut(num):
    b=[]
    while len(b)<num:
        temp = int(input("숫자를 세번 입력하세요."))
        b.append(temp)
    return b
    
#비교한다.
def Compare(a,b):
    strike=0
    ball=0
    for j in range(len(a)):
        for i in range(len(b)):
            if a[j]==b[i] and i==j:
                strike = strike + 1
            elif a[j]==b[i] and i!=j:
                ball = ball + 1
    print("%d strike and %d balls"%(strike,ball))
    return strike

a = makeNumber(3)
while Compare(a,b)!=3:
    b = inPut(3)
#print("print b =",b)
#print("%dstrikes and %dballs"%(strike,ball))

"""
while :
    for j in range(3):
        for i in range(3):
            if a[j]==b[i] and i==j:
                strike = strike + 1
            elif a[j]==b[i] and i!=j:
                ball = ball + 1
    print("%d strike and %d balls"%(strike,ball))
    
print("good")
"""
