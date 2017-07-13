#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 14:18:16 2017

@author: innersme
@subject: list example
"""

def Print(string):
    print("\n")
    print("-----%s-----"%string)

"""
# 다른 데이터 타입도 출력 가능하다.; 이 경우 데이터 타입이 다르므로 쓸모가 없음.
temps = [1, 2, 3, 5, 6, 3.0, True, 'hi']
print(temps)

# len 함수는 리스트 항목의 개수를 출력한다.
Print("len함수")
length = len(temps)
print(length)

# list 함수는 문자열을 분리하여 리스트로 바꿔준다.
Print("list함수")
value = list(range(10))
print(value)

#for 문과 결합.
Print("for문과 결합")
for i in temps:
    print(i)
    
Print("list함수의 활용")
str = 'Hello' # Hello라는 문자열을 str변수에 입력
print("str변수 출력")
print(str)
strlist = list(str)
print("list함수를 사용한 list(str)출력")
print(strlist)

Print("str과 for문")
for c in str:
    print(c)
    
#string데이터는 개개별로 list
Print("숫자로 된 문자열의 for문 활용")
number = '123456'
for item in number:
    print(item)

Print("숫자로 된 문자열의 sum")
numbers = '12345698'
sum = ''
for item in numbers:
    sum = sum + item
print(sum)

# 숫자를 가지고 있는 문자는 함수를 통해서 숫자로 변경이 가능하다.
Print("숫자로 된 문자열의 sum(int함수를 이용하여, 숫자로 변환)")
numbers = '12345698'
sum = 0
for item in numbers:
    sum = sum + int(item)
print(sum)

Print("list와 len함수, list[i]와 for문의 활용")
numbers = [2, 8, 9, 1, 6]
for i in range(len(numbers)): #len(numbers) = 5  즉, range(5)
    print(numbers[i]) #numbers[0, 1, 2, 3, 4, 5] #why? range(5) = [0,1,2,3,4]
    
"""

"""
문제: numbers를 오름차순 순서로 배열하시오.
"""

numbers = [2, 8, 9, 1, 6]

    