#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 09:41:12 2017

@author: innersme
"""


"""
1000에서 2000 사이의 소수(prime number)를 판별하여 출력하시오.

소수: 1과 자기자신만으로 나누어지는 수
for j in range(1,j+1):
    if number % j == 0:
        count = 1

"""

number = 1000
count = 0
for i in range(number):
    # 만약 주어진 숫자가 2에서 자기 자신까지 나누었을 때,
    if number % (i+1) == 0:
        #나누어진다면 count를 1씩 증가시킨다. 
        count = count + 1
#그리고 그 count가 2라면, 소수이다.
if(count == 2):
    print("소수")
#아니라면, 소수가 아니다.
else :
    print("합성수 count = %d"%count)

#주어진 수가 2에서 100까지 소수는 몇 개니?

#count_sum_ex는 for에 독립적이어야 한다.
#누적시키는 아이디어 많이 쓰이지 ?
#초기화를 한다. 
count_sum_ex = 0
for j in range(2,101):
    number_ex = j
    count_ex = 0
    for i_ex in range(number_ex):
        # 만약 주어진 숫자가 2에서 자기 자신까지 나누었을 때,
        if number_ex%(i_ex + 1)==0:
            #나누어진다면 count를 1씩 증가시킨다. 
            count_ex = count_ex + 1
    #그리고 그 count가 2라면, 소수이다.
    if(count_ex == 2):
        #number_ex가 나누어 지는 수가 2로 나누어진다면, count_sum_ex를  1씩 증가시킨다. 
        count_sum_ex = count_sum_ex + 1
#count_sum_ex는 for에 독립적이어야 한다.
print("개수는 %d개"%count_sum_ex)

# 25개 입니다. 


    #아니라면, 소수가 아니다.    
    #else :
    #    print("합성수 count = %d"%count_ex)
        
"""
count = 0
# number 가 1000에서 2000으로 주어진다.
for i in range(1000,2001):
    # 만약 주어진 i가 (2에서 i-1)로 나누었을 때 
    # 나누어지는 수가 한개 도 없을 때, i는 소수이다.
    for j in range(2,i):
        if i%j==0:
            count = count + 1
"""