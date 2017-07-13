#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 10:26:50 2017

@author: innersme
module 
"""

#데이터를 변형 시킴.
def make_dataset(raw_data):
    

        inner_list.append(raw_data[i][30:31])
        outer_list.append(inner_list)
    return outer_list

#표기법에 대해 볼 줄 알아야 한다. 
#기반이 되는 것들 
#실습시간을 주면 60% 
def get_max_list(outer_list, index):
    for i in range(len(outer_list-1)):
        for j in range(i+1,len(outer_list)):
            if outer_list[i][index] < outer_list[j][index]:
                temp = outer_list[i]
                outer_list[i] = outer_list[j]
                outer_list[j] = temp
            elif outer_list[i][index] == outer_list[j][index]:
                if outer_list[i][0] > outer_list[j][0]:
                    temp = outer_list[i]
                    outer_list[i] = outer_list[j]
                    outer_list[j] = temp
                    
    return outer_list