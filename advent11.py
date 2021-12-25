# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 21:37:07 2021

@author: Karol
"""

f = open("tmp.txt", "r")
mapa = []
mapa.append([-1]*12)
for line in f:
    l = [-1]
    for el in line[:-1]:
        l.append(int(el))
    l.append(-1)
    mapa.append(l)
mapa.append([-1]*12)

compare = [[-1]*12]
for i in range(10):
    line = [-1]
    for j in range(10):
        line.append(0)
    line.append(-1)
    compare.append(line)
compare.append([-1]*12)    

res = 0
for i in range(10000):
    for j in range(1,11):
        for m in range(1,11):
            mapa[j][m]+=1
    change = True
    to_clear = []
    while change:
        change = False
        for j in range(1,11):
            for m in range(1,11):
                if mapa[j][m] > 9:
                    change = True
                    mapa[j][m] = 0
                    to_clear.append([j,m])
                    res+=1
                    mapa[j+1][m] +=1
                    mapa[j-1][m] +=1
                    mapa[j][m+1] +=1
                    mapa[j][m-1] +=1
                    mapa[j+1][m+1] +=1
                    mapa[j+1][m-1] +=1
                    mapa[j-1][m+1] +=1
                    mapa[j-1][m-1] +=1                    
    for ide in range(12):
        mapa[ide][0] = -1
        mapa[ide][11] = -1
        mapa[0][ide] = -1
        mapa[11][ide] = -1
    for el in to_clear:
        mapa[el[0]][el[1]] = 0
    to_clear = []
    if mapa == compare:
        print(i+1)
        break
    
print(res)
                    