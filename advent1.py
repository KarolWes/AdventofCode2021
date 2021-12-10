# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 20:37:07 2021

@author: Admin
"""

n = 0
prev = 602
line_counter = 0
a = 199
b = 203
c = 200
act = 0

f = open("input.txt", 'r')
#act = (int)(line)
#  if act > prev:
#      n+=1
#  prev = act'''
for line in f:
    if line_counter < 3:
        act += (int)(line)
        line_counter +=1
    else:
        new_val = (int)(line)
        print(act)
        if act > prev:
            n+=1
        prev = act
        act -= a
        a = b
        b = c
        c = new_val
        act += new_val
        
    
if act > prev:
    n+=1 
print(n)