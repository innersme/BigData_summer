# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 16:31:06 2017

@author: user
"""
import random
word = 'internationalization'
length = int(len(word)*0.2)
position_index = []
for i in range(length):
    position_index.append(random.randrange(len(word)))

print(position_index)
for i in range(len(word)):
        if i in position_index:
            print('_',end='')
        else: 
            print(word[i],end='')
            
# 비교 로직
letter = input('input letter >>> ')
# word와 letter의 인덱스만 비교.
for i in position_index:
    if letter == word[i]:
        print("존재한다. ")
    else:
        print("존재하지 않음")