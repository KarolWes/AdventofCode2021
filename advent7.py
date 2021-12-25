# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 12:32:22 2021

@author: Karol
"""

def subset(a,b):
    res = True
    for el in a:
        res = res and (el in b)
    return res

def difset(a, b):
    #a must be smaller
    res = []
    for el in b:
        if not(el in a):
            res.append(el)
    return res

def sumset(a,b):
    res = a
    for el in b:
        if not(el in res):
            res.append(el)
    return sorted(res)

f = open("input.txt", "r")
res = 0
for line in f:
    record = line.split("|")
    tab = ['']*10
    tmp = record[0].strip()
    tmp = tmp.split()
    for el in tmp:
        if len(el) == 2:
            tab[1] = sorted(el)
        elif len(el) == 3:
            tab[7] = sorted(el)
        elif len(el) == 4:
            tab[4] = sorted(el)
        elif len(el) == 7:
            tab[8] = sorted(el)
        
    for el in tmp:
        test = sorted(el)
        if len(test) == 5:
            if subset(tab[1], test):
                tab[3] = test
            elif len(difset(tab[4], test)) == 2:
                tab[5] = test
            else:
                tab[2] = test
                
            
        elif len(test) == 6:
            if len(difset(test, tab[1])) == 1:
                tab[6] = test
            elif subset(tab[4], test):
                tab[9] = test
            else:
                tab[0] = test
    
    
    
    record = record[1].strip()
    record = record.split()
    num = 0
    for el in record:
        test = sorted(el)
        for i in range(10):
            if test == tab[i]:
                num*=10
                num+=i
    print(num)
    res+=num
print(res)