# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 11:03:43 2017

@author: user
"""

# 시도

weekday = 7
weeknum = 4

print("S\tM\tT\tW\tT\tF\tS")
for i in range(weeknum):
    for j in range(weekday):
            print("%d\t"%(j+1),end='')
    print("")
    
print("\n")
print("S\tM\tT\tW\tT\tF\tS")
for j in range(weekday):
    print("%d\t"%(j+1),end='')

print("\n")
print("S\tM\tT\tW\tT\tF\tS")
for i in range(7):
    print("%d\t"%(i+1),end="")
print("\n") 

# 여기서 부터 강의
print("Sun\tMon\tTue\tWed\tTur\tFri\tSat")
for i in range(31):
    print("%d\t"%(i+1),end="")
    # (i+1)이 7의 배수일때(7로 나누어 떨어질 때), 한 줄
    if (i+1)%7==0:
        print("")
    # 그렇지 않으면, 
    else:
        print("",end="")
        
