# -*- coding: utf-8 -*-
"""
week_tue_ex03.py string변수
Created on Tue Jul  4 14:30:00 2017

@author: user

"""
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

#list in list

list2list = [
        [1,2,4,6,8],
        [2,4,16,27,81]
        ]

print(len(list2list))       # 2: 요소가 2개다.
print(len(list2list[1]))       # 5: list2list[0] = 5    
print(list2list[1][2])      # 16: list2list[1][2] 

#key값은 일반적으로 string을 사용한다. 
grades = {"Joel":['1254',80,20,90], "Tim":['2314',87,95,95]}

#예외처리 try: except Errorcode:
try:
    #dict 변수
    joe_grade = grades["Joel"]
except KeyError:
    print("no grade for ")

#print dict
print(joe_grade)
print(grades.keys())
print(grades.values())

names = grades.keys()
for name in names:
    print("key=%s, values=%s"%(name, grades[name]))
    
"""
"""
s = set([1,2,2,3,4])

print(len(s))

#set는 중복을 허락하지 않는다. 
#set 함수를 list 로 교환할 수 있다.
#자유롭게 set < - > list로 변경이 가능하다.
print(list(s))

#만들 숫자를 저장하는 숫자를 set로 해버리면, 중복check할 필요가 없다. 
# set = 집합
"""

s1 = set([1,2,3,4])
s2 = set([3,4,5,6])
# 교집합
print(s1.intersection(s2))
# 합집합
print(s1.union(s2))
# 차집합 s1-s2
print(s1.difference(s2))

print(s1 & s2)
print(s1 | s2)
print(s1 - s2)