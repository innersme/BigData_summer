# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 11:03:43 2017

@author: user
"""

"""
try
for문을 두 번 쓰기를 시도 했음.-> 1-7만 4번 반복됨.
마지막 숫자에다 +1씩 추가한 것을 그 다음 for문의 첫 숫자로 적을려고 했음.

range(처음 숫자, 반복횟수-1)

"""

weekday = 7
weekday_2 = weekday
weeknum = 4
ini = 0

print("----try1----")
print("S\tM\tT\tW\tT\tF\tS")
weekday_2 = weekday
for i in range(weeknum):
    for j in range(weekday):
            print("%d\t"%(j+1),end='')
    print("")
    

    
print("\n----try2----")
print("S\tM\tT\tW\tT\tF\tS")
for j in range(weekday):
    print("%d\t"%(j+1),end='')

print("\n")
print("\n")

"""
answer -> if문 이용.

"""
print('----answer----')
print("Sun\tMon\tTue\tWed\tTur\tFri\tSat")
for i in range(31):
    print("%d\t"%(i+1),end="")
    # (i+1)이 7의 배수일 때(7로 나누어 떨어질 때), 한 줄을 내린다.
    if (i+1)%7==0:
        print("")
    # 그렇지 않으면, 그대로 둔다.
    else:
        print("",end="")
print("\n")
print("\n")

"""
answer2 
목표: 하드코딩을 없애자!
변수와 %d %s를 사용.
일반화 하기. 

"""

year = 2017
month = "May"
num_day = 31
blank = 1

print('\t\t\t%d %s'%(year,month))
print("Sun\tMon\tTue\tWed\tTur\tFri\tSat")
print('\t'*blank,end="")
for i in range(num_day):
    print("%d\t"%(i+1),end="")
    if (i+1+blank)%7==0:
        print("")
    else:
        print("",end="")