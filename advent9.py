# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 13:18:59 2021

@author: Karol
"""


def BFS(start):
    res = 0
    qu = queue.Queue()
    qu.put(start)
    while not(qu.empty()):
        u = qu.get()
        if newmap[u[0]][u[1]] == '0':
            newmap[u[0]][u[1]] = '1'
            res += 1
            if newmap[u[0]][u[1]+1] == '0':
                qu.put([u[0], u[1]+1])
            if newmap[u[0]+1][u[1]] == '0':
                qu.put([u[0]+1, u[1]])
            if newmap[u[0]][u[1]-1] == '0':
                qu.put([u[0], u[1]-1])
            if newmap[u[0]-1][u[1]] == '0':
                qu.put([u[0]-1, u[1]])
        
    return res
    
import queue
res = 0
f=open("input.txt","r")
mapa=[]
for line in f:
    mapa.append(line.strip())
    
for i in range(len(mapa)):
    
    for j in range(len(mapa[i])):
        test = True
        if i == 0:
            test=test and (mapa[i][j]<mapa[i+1][j])
            if j == 0:
                test=test and (mapa[i][j]<mapa[i][j+1])
            elif j == len(mapa[i])-1:
                test=test and (mapa[i][j]<mapa[i][j-1])
            else:
                test=test and (mapa[i][j]<mapa[i][j-1])
                test=test and (mapa[i][j]<mapa[i][j+1])
        elif i == len(mapa) -1:
            test=test and (mapa[i][j]<mapa[i-1][j])
            if j == 0:
                test=test and (mapa[i][j]<mapa[i][j+1])
            elif j == len(mapa[i])-1:
                test=test and (mapa[i][j]<mapa[i][j-1])
            else:
                test=test and (mapa[i][j]<mapa[i][j-1])
                test=test and (mapa[i][j]<mapa[i][j+1])
        else:
            test=test and (mapa[i][j]<mapa[i+1][j])
            test=test and (mapa[i][j]<mapa[i-1][j])
            if j == 0:
                test=test and (mapa[i][j]<mapa[i][j+1])
            elif j == len(mapa[i])-1:
                test=test and (mapa[i][j]<mapa[i][j-1])
            else:
                test=test and (mapa[i][j]<mapa[i][j-1])
                test=test and (mapa[i][j]<mapa[i][j+1])
        
        if test:
            res+=int(mapa[i][j])+1
print(res)
newmap = []
newline = []
basins = []
res = 0
f.close()
q = queue.Queue()
f = open("input.txt", "r")
newmap.append(['1']*102)
for line in f:
    line = line.strip()
    newline.append('1')
    for el in line:
        if el == '9':
            newline.append('1')
        else:
            newline.append('0')
    newline.append('1')
    newmap.append(newline)
    newline = []
newmap.append(['1']*102)
for i in range(len(newmap)):
    for j in range(len(newmap[i])):
        if newmap[i][j]=='0':
            q.put([i,j])



while not(q.empty()):
    u = q.get()
    if newmap[u[0]][u[1]] == '0':
        basins.append(BFS(u))

basins = sorted(basins, reverse=True)
print(basins[0]*basins[1]*basins[2])

