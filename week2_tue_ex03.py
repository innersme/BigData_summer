# -*- coding: utf-8 -*-
"""
week_tue_ex03.py string변수
Created on Tue Jul  4 14:30:00 2017

@author: user

"""

# 데이터는 한줄로 여러개의 정보를 합쳐서 집어넣는다
# 3,5,3,3,3 이름 학번 국어 영어 수학 점수 순으로
info = 'kim12365100 89 87'
print(info[:3])
print(info[3:8])  #[a,b) 
print(info[8:11])
print(info[11:14])
print(info[14:])

infov = "kim,12365,100,89,87"
r = infov.split(",")
sum_r = 0
for i in range(2,5):
    sum_r = sum_r + int(r[i])
print(r)
print("sum = %d"%sum_r)
for item in r:
    print(item)
    
    
data = [1,2,3,4,5]
print(data[::-1])