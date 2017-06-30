#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 16:41:35 2017

@author: innersme
"""

import random #키워드 모듈명
balls =[]
for i in range(6):
    rnd = random.random()
    value = (rnd*45*100//100)+1 # 바운더리를 정할 것이다.  rnd*(범위)*소수점이하 버림
    #중복제거
    if value in balls:
        print(value)
        continue
    balls.append(int(value)) #append 리스트에 추가
    
print(balls)
