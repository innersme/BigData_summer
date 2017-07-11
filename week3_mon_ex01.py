# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 09:18:25 2017

@author: user
"""

file = open("subject.txt", 'r')
lists = file.readlines()
a = []
number = len(lists)
for i in range(number):
    a.append(lists[i].split('\t'))



sum = 0
for j in range(number):
    sum = sum + float(a[j][4])

print(sum) # 계절 
# 새로운 리스트 생성

def change(string):
    n = 0
    if string == 'A+':
        n = 4.5
    elif string == 'A0':
        n = 4 
    elif string == 'B+':
        n = 3.5
    elif string == 'B0': 
        n = 3
    elif string == 'C+': 
        n = 2.5
    elif string == 'C0': 
        n = 2
    return n





sum2 = 0
for j in range(number):
    sum2 = sum2 + (float(change(a[j][5])/float(a[j][4]))
    print("%s,\t\t학점=%.1f,\t학점합계=%.1f"%(a[j][3],float(change(a[j][5])),sum2))

print(sum2)
print(sum2/number)


file.close()
