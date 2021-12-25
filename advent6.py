# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 07:52:38 2021

@author: Karol
"""

def count(el):
    if el == 0:
        tmp.append(8)
        el=6
    else:
        el-=1

f= open("input.txt", "r")
tab = []
l = f.readline()
l = list(map(int, l.split(",")));
fout = open("res.txt", "w")
for el in l:
    fout.write(str(el))
    fout.write("\n")
fout.close()
for el in l:
    tab.append(el)
tmp = []
tab2 = []
tab3 = []
tab4 = []
tab5 = []
for gen in range(256):
    print(gen)
    for i in range(len(tab)):
        if tab[i] == 0:
            tmp.append(8)
            tab[i] = 6
        else:
            tab[i] -= 1
    for el in tmp:
        tab.append(el)
    tmp = []
            
            
print(len(tab)+len(tab2))
        