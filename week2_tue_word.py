# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 17:06:16 2017

@author: user
"""

"""
    만약에 word_l의 원소를 다 검사하는데, 
    이 원소중에 'p'와 일치하는 성분이 있다면,
    p를 '_'로 바꿔라
"""

"""
print(len(word_l))
for item in len(word_l):
    print(word_l[item])
"""

# 제외 함수
def exclude(word,e_word):
    #입력받은 단어를 list로 변경한다.
    word_l = list(word)
    for item in range(len(word_l)):
        if e_word == word_l[item]:
            word_l[item] = '_'
    print("".join(word_l))




exclude('pear','e')