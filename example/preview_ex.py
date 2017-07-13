#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 15:04:47 2017

@author: innersme

문제: numbers를 오름차순 순서로 배열하시오.
"""

def Print(string):
    print("\n")
    print("-----%s-----"%string)

"""
1) 만약 0번째 > 1번째 라면, 바꾼다
2) 0번째 -> n-1번째 반복,
3) 1)-2) 계속반복. (언제까지? 모든 i번째 < i+1번째 가 될 때까지 )
"""
Print("MyAnswer")

def Sort(i):
    if numbers[i] > numbers[i+1]:
        temp = numbers[i]
        numbers[i] = numbers[i+1]
        numbers[i+1] = temp

Print("변환 전")
numbers = [2, 8, 9, 1, 6, 3]
print(numbers)
for j in range(len(numbers)-1):
    for i in range(len(numbers)-1):
        Sort(i)

Print("변환 후")
print(numbers)

Print("합계")
sum = 0
for i in numbers:
    sum = sum + i
print(sum)


"""
1) 0번째 number를 추출한다.
2) 1번째 number부터 n번째 number까지 0번째 넘버보다 작은수가있는지 확인하고,
3) 있으면 Sort
4) 1)을 0부터 n-1까지 반복한다. 
"""

Print("Solution")
numbers = [2, 8, 9, 1, 6, 3]
Print("변환 전")
print(numbers)
for i in range(len(numbers)-1):
    for j in range(i+1, len(numbers)):
        if numbers[i]>numbers[j]:
            temp = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = temp
Print("변환 후")   
print(numbers)
