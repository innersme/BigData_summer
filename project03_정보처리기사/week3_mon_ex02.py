# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 15:48:52 2017

@author: user
"""

file = open("Abc1115.txt", 'r')
lines = file.readlines()

def select(lists):
    inner_lists = []
    inner_lists.append(lists[0:6])
    inner_lists.append(lists[6:10])
    inner_lists.append(lists[10:13])
    inner_lists.append(lists[13:16])
    inner_lists.append(lists[16:19])
    inner_lists.append(lists[19:22])
    inner_lists.append(lists[22:25])
    inner_lists.append(lists[25:28])
    inner_lists.append(lists[28:29])
    inner_lists.append(lists[29:30])
    inner_lists.append(lists[30:31])
    return inner_lists

sum = 0
for i in range(len(lines)):

    if int(select(lines[i])[7]) > 150:
        
        if select(lines[i])[9] == 'A':
            sum = sum + (int((select(lines[i])[3])) + 5 ) 
        
        elif select(lines[i])[9] == 'B':
            sum = sum + (int((select(lines[i])[3])) + 15 ) 
            
        else:
            sum = sum + (int((select(lines[i])[3])) + 20 ) 
    
print("문제3 = ",sum)

