# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 13:47:37 2017

@author: user
2. 단어를 출력하는 함수 (사용자에게 단어하나를 출력) 
"""

"""
# 추출한 단어에서 
# 단어 입력함수
coffee가 주어지면 c가 바뀌어있다.

바뀐 원소num을 조회한다.
abcd 와 abc_ 를 조회하는데,
[3]이 출력
"""

import random
#wordlist: string

wordlist = 'cofe,aply,pocket,google,water,programming,disappointed,neighbor,pronunciation,dangerous'

#wordlist: list
word = wordlist.split(',')


# 제외 함수
def changeword(word,e_word):
    #입력받은 단어를 list로 변경한다.
    word_l = list(word)
    for multi in range(len(word)):
        for item in range(len(word_l)):
            if e_word == word_l[item]:
                word_l[item] = '_'        
    word_p = "".join(word_l)
    return word_p

#변경할 단어 갯수 선정 함수
def wordnumber(word):
    number = 1
    if len(word) > 8:
        number = 2
    return number

#단어 출력함수
 
# 바뀐 함수와 바뀌기 전 index를 return
def isdifferent(wordone,wordtwo):
    i = 0
    num = []
    for n in range(len(wordone)):
        if wordone[n] == wordtwo[n]:
            i = i + 1
        else:
            num.append(i)
    return num

# word list를 changedlist로 return 하는 함수
def outputlist(word):
    changedlist=[]
    for i in range(len(word)):
        changedlist.append(changeword(word[i],random.choice(word[i])))
    return changedlist

#인덱스를 입력받아 word 를 changedword로 
def change(word,charword,index):
    chword = word[:index]+charword+word[index+1:]
    return chword


changed = outputlist(word)
#word만큼 반복


for i in range(len(word)):
    #문제 출제
    while True:
        #맞을때 까지 반복   
        print(changed[i])
        #nubmer = 단어와 변경된 단어의 index 추출
        number = isdifferent(word[i],changed[i])
        mul = wordnumber(word) - 1
        #changedone[i] index만큼 반복.
        char = input("빈칸에 단어를 입력하세요.")
        change = change(changed[i],char,number[0])
            
        if change == word[i]:
            print("입력값: %s, 정답입니다. 다음 단어로 넘어가세요.\n"%change)
            break
#        elif char==1:
#            break
        else:
            print("입력값: %s, 틀렸습니다. 다시 시도하세요.\n"%change)

print("10개를 모두 맞추셨습니다. 축하드립니다.")
