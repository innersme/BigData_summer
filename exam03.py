# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 13:31:15 2017

@author: user
@example3: 구구단
"""
#추상화를 얼마나 많이 하느냐

print("----강의----")
number = 3
for i in range(9):
    print("%dX%d=%2d"%(number,i+1,3*(i+1)))

print("\n"*3)

print("과제: 구구단 2단 - 9단을 만드시오")
for j in range(8):
    number_assign1 = j+2
    for i in range(9):
        print("%dX%d=%2d"%(number_assign1,i+1,(j+2)*(i+1)))
    print()

"""
line18: for j in range(8):

    
"""


print("""
      2중 for문;
      패턴을 읽어내야 한다. 
      """)

print("강의: 구구단 2단 - 9단을 만드시오")

print("""
      너무 길어
      """)