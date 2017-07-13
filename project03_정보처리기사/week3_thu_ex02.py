#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 10:36:49 2017

@author: innersme
정보처리기사 예제 실기
"""


outer_list = my_module.make_dataset(data)
print(len(outer_list))
print(outer_list[0])

#프로그래밍 사용법을 살펴봐 solve_1=[]
solve_1 =[]
for line in outer_list:
    if line[9] == 'A' or line[9] =='B':
        sum = int(line[2])+int(line[3])
        line.append(sum)
        solve_1.append(line)
        
# 다른 사람의 코드를 익혀야 하느냐, 본인이 시도한 방식
# 매번 반복해서 짜면 코드에서 줄어든다.         
print(solve_1[0])
result = my_module.get_max_list(solve_1,11)
