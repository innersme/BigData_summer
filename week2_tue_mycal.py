# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 11:03:43 2017

@author: user

문제: 입력값이 존재하는 달력을 출력하는 함수를 만들어 보시오. 

#사용자에게 팔기 위해서는, 사용자가 불편하면 안된다.
#프로그램은 개발자의 입장에서 보면 안된다. 

좋은 프로그램은 사람이 개입하면 안된다. 자동화가 이루어 져야한다.

정보가 주어지면 함수상에서 되도록이면 처리해야한다. 

하나의 변수가 여러개의 값을 가진다면?

12개의 변수가 각각의 값을 가진다면, 
1번 고객부터 1000만번째 고객 사람의 개입없이 
자동으로 첫 번째값, 두번째 값, ... , n번째 값.

리스트 -> 자료를 순차적으로 관리한다.
같은 의미의 변수는 하나로 하고, 여러개의 값을 가지고 싶다면, list사용

data를 순서대로 취급하는 방법 
소수의 data로는 분석을 신뢰할 수 없다. 
많은 데이터를 자동화할 때, 사람의 개입이 있으면 안된다. 

'순서대로' 모아서 다루는 것이 => list이다.

데이터의 CRUD작업 
1.생성 2.조회 3.갱신 4.삭제

핵심로직과 관리로직

"""
import calendar
def viewMonth(year,_month):
    result = calendar.monthrange(year,_month)
    #_변수를 쓰는 이유? 본문의 내용 변경을 최소화 하기 위해
    #calendar.monthrange[0]의 결과가 index로 출력되므로 보정을 위해 + 1 이 필요하다. 
    space = result[0] + 1 
    month = _month
    num_day = result[1]
    #리스트 : 
    #정보의 중복; 첫 날을 계산해내는 알고리즘을 만든다.
    
    #num_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    #num_day = num_days[_month - 1]
    #spaces = [0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5]
    
    
    print('\t\t\t%d %d'%(year,month))
    print("Sun\tMon\tTue\tWed\tTur\tFri\tSat")
    print('\t'*space,end="")
    for i in range(num_day):
        print("%d\t"%(i+1),end="")
        if (i+1+space)%7==0:
            print("")
        else:
            print("",end="")
    print("\n")
    return
