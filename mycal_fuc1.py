# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 11:03:43 2017

@author: user

answer2 
목표: 하드코딩을 없애자!
변수와 %d %s를 사용.
일반화 하기. 


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
        

문제: 입력값이 존재하는 달력을 출력하는 함수를 만들어 보시오. 
"""
def viewMonth(_blank,_month,_num_day):
    year = 2017
    #_변수를 쓰는 이유? 본문의 내용 변경을 최소화 하기 위해
    month = _month
    num_day = _num_day
    blank = _blank
    
    print('\t\t\t%d %d'%(year,month))
    print("Sun\tMon\tTue\tWed\tTur\tFri\tSat")
    print('\t'*blank,end="")
    for i in range(num_day):
        print("%d\t"%(i+1),end="")
        if (i+1+blank)%7==0:
            print("")
        else:
            print("",end="")
    
    return

viewMonth(6, 7, 31)

"""

"""