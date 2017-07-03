#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 10:51:00 2017

@author: innersme
R은 패키지이다. 프로그래밍 언어가 아님!

    
"""

print("week2")

#list는 []를 사용한다. 
a = [1,2,3]
print(type(a))


# 만약 ()를 쓴다면?
b = (1,2,3)
print(type(b))

# a[0] 데이터를 수정하자.
a[0] = 10
print(a)

# b[0] 데이터를 수정하자.
# b[0] = 100
# type 'tuple'은 수정이 불가능하다. 
print(b)

#index는 i,j,k로 사용, data는 명시할 수 있어야한다.
print("index 출력")
for item in a:
    print(item)
    
print("data 출력")
for i in range(len(a)): #len(a): a의 크기
    print("%d => %d"%(i,a[i])) #index와 item 을 출력

print("index와 data를 동시에 출력 enumerata(a)")
for i, item in enumerate(a): #enumerate = index와 data
    print("%d->%d"%(i,item))

print("[1에서 45까지 random출력]")    
#모듈 import
import random 
rnd = random.random()
#0.** 에서 44.**까지 rnd*45(범위지정)+1(1에서 45까지)
temp = int(rnd*45)+1
print(temp)

"""
100에서 999까지 int(rnd*900)+100
"""

temp_hun = int(rnd*900)+100

"""
0에서 9
10에서 99
100에서 999
... 일반화 하자.
"""
print("[0-9 or 10-99 or 100-999 or 1000-9999]") 

"""
try:
a = [1,2,3]

def makeNumber(num):
    temp_num = int(random.random()*9*10**(num-1))+10**(num-1)
    print(temp_num)
필요한 지식: ^을 나타내는 파이썬 문법은 **이다. 

answer:
"""
def makeNumber(num):
    number = int(random.random()*(10**num-10**(num-1)))+10**(num-1)
    return number

result = makeNumber(3)
print('result = %d'%result)