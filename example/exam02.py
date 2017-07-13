# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 09:17:05 20174

@author: user
for 문 사용하기
"""


number = 123456
sum = 0

for i in range(6):
    temp = number % 10
    print(temp)
    sum = sum + temp
    number = number // 10 

print('sum =>' , sum)

print('range(1,10) & i')
for i in range(1,10):
    #print("2 X",i,"=",i*2)
    print("2X%d=%d"%(i,2*i))
    
print('\n\nrange(9) & i+1')
for i in range(9):
    #print("2 X",i,"=",i*2)
    print("2X%d=%d"%(i+1,2*(i+1)))
    
# range(1,10)은 안좋은 습관? 여기에 논리가 들어가
# 복잡해진다. 
# range(9) & i+1
