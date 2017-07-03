#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 16:02:20 2017

@author: innersme
"""
import random
#stringtype Number 입력받는데, 출력값은 flag
#숫자가 같니 isSameNumber?

"""
makeNumber함수 설명
1. num을 입력받는다(num=자리수, 예를들어 num=3, 세자리수 = 100-999)
int(random.random()*(10**num-10**(num-1)))+10**(num-1)
2. 숫자를 만들고(random) number에 대입
3. 만약 number에 중복되어있는 문자가 존재하면, 다시 숫자를 만든다.
4. 숫자를 string 형식으로 반환

숫자를 만들어내는 것 뿐. 
"""

#숫자 만들기 (num) 함수를 만들기 위해서는 input값 필요해
def makeNumber(num):
    #계속 반복한다. 무엇을? 
    #몇번 반복하는지 몰라 -> while사용
    while True:
        #입력받은 num자리수
        #makeNumber(2) = 10 - 99 (string type)
        #int(random*900)+100 = (0-900) + 100 = 100-1000 => 100-999
        #int(random*9)+1 = (0-9) + 1 = 1 - 10 => 1 - 9
        #random*(10^num-10^(num-1))+10^(num-1)
        number = int(random.random()*(10**num-10**(num-1)))+10**(num-1)
        #작업이 다르면 서로 분리해
        #같은게 있니 check = True or False
        check = isSameNumber(str(number))
        #중복되었니? not False = True 
        #check 
        if not check:
            break
            
    #return number 값.string type
    return str(number)    


"""
isSameNumber함수 설명
1. abc,,,z를 입력받는다
2. flag설정 = 기본 False (만약, a,b,c중 서로 문자가 같으면 True)
3. a와 a이외의 문자 (b,c,d,...,z)와 비교
4. b와 a,b이외의 문자 (c,d,...,z)와 비교
5. c,...,z-1와 그다음 문자와 비교
6. 만약 3-5과정중 같은 문자가 있으면 flag=True로 대입하고 break
7. 출력값 flag = (True or Flase)
"""
def isSameNumber(strNumber):
    #같지 않다(초기값)
    flag = False
    #i = [0,1,2,...,len(strNumber)-1]
    for i in range(len(strNumber)-1):
        # j = [i+1, i+2, ... , len(strNumber)-1]
        for j in range(i+1,len(strNumber)):
            #만약 a,b,c,d,..., 중 서로 한개가 갖은게 있다면,
            if strNumber[i] == strNumber[j]:
                #flag = True대입하고 if문 빠져나와
                flag = True
                break
                #여기서 return 하는 습관이 있다. 
                #if문에서는 가능하지만, for문이 끝난다
    return flag

"""
compareNumber(target,guess)
target과 guess 각 자리별로 비교하는데,
1.strike 
(target[0] == guess[0]) and 0==0 이라면, strike
2.ball
(target[0] == guess[1]) and 0!=1 이라면, ball
target 과 guess 의 len만큼 반복하자.
strike와 ball

"""
def compareNumber(targetNumber,guessNumber):
    #초기화
    strike = 0
    ball = 0
    #target, guess의 길이 범위
    for j in range(len(targetNumber)):
        for i in range(len(guessNumber)):
            #number와 index 모두 같으면 strike
            if targetNumber[j]==guessNumber[i] and i==j:
                strike = strike + 1
            #number는 같지만 index가 같지 않으면 ball
            elif targetNumber[j]==guessNumber[i] and i!=j:
                ball = ball + 1
    #처리 로직
    #python은 다른 프로그래밍 언어와 다르게 return 값을 list로 받을 수 있다. 
    #return [strike, ball] 과 같이 return 값을 list로 출력할 수 있다. 
    #result[0], result[1] 이런식으로 출력하면 됨!
    #return[0] = strike , return[1] = ball
    return [strike,ball]
