import string
import math
import queue
def save(line):
    depth = 0
    res = []
    for char in line:
        if char == '[':
            depth+=1
        elif char == ']':
            depth -=1
        elif char in string.digits:
            res.append([int(char), depth])
    return res
            
def explode(line):
    to_delete = []
    # maxi = 0
    # for el in line:
    #     maxi = max(maxi, el[1])
    # maxi = max(maxi, 5)
    res = False
    for i in range(len(line)-1):
        if line[i][1] > 4 and line[i][1] == line[i+1][1]:
            if i > 0:
                line[i-1][0] += line[i][0]
            line[i][0] = 0
            line[i][1] -=1
            if i+1 < len(line)-1:
                line[i+2][0] += line[i+1][0]
            to_delete.append(i+1)
            res = True
            break
    deleted = 0
    for el in to_delete:
        line.pop(el-deleted)
        deleted +=1
    return res

def ssplit(line):
    res = []
    correction = False
    for el in line:
        if el[0] > 9 and not(correction):
            left = [math.floor(el[0]/2), el[1]+1]
            right = [math.ceil(el[0]/2), el[1]+1]
            res.append(left)
            res.append(right)
            correction = True
        else:
            res.append(el)
    return res

# def reduce(line):
#     test = True
#     while test:
#         while test:
#             test = explode(line)
#         test = True
#         counter = 0
#         while test:
#             tmp = ssplit(line)
#             test = (tmp != line)
#             line = tmp
#             counter +=1
#         test = (counter > 1)
#     return line

def split_check(line):
    res =0 
    for el in line:
        if el[0] > 9:
            res+=1
    return res

def explode_check(line):
    res = 0
    for el in line:
        if el[1] >4:
            res +=1
    return res

def reduce(line):
    q = queue.LifoQueue()
    q.put("e")
    while not(q.empty()):
        top = q.get()
        print(line)
        if top == "e":
            last = split_check(line)
            test = explode(line)
            if test:
                q.put("e")
            new = split_check(line) - last
            if new > 0:
                for _ in range(new):
                    q.put("s")            
        else:
            last = explode_check(line)
            line = ssplit(line)
            new = explode_check(line)-last
            if new > 0:
                q.put("e") 
    return line

def add(a, b):
    res = []
    for el in a:
        el[1] +=1
        res.append(el)
    for el in b:
        el[1] +=1
        res.append(el)
    return res

# def pprint(line):
#     res = ''
#     act_depth = 0
#     for el in line:
#         dif = el[1] - act_depth
#         if dif > 0:
#             res+='['*dif
#             res+=str(el[0])
#             res+=','
#         elif dif < 0:
#             res+=']'*dif
#             res+=','
#             res+=str(el[0])
#         else:
#             res+=str(el[0])
#             res+='],'
#             el[1] -=1
#         act_depth = el[1]
#     print(res)

def pprint(line):
    for el in line:
        print( el[0], end = ' ')
    print()

snailfish = []
f = open("tmp.txt", "r")
for line in f:
    snailfish.append(save(line))
for i in range(1, len(snailfish)):
    snailfish[0] = add(snailfish[0], snailfish[i])
    snailfish[0] = reduce(snailfish[0])
snailfish[0] = reduce(snailfish[0])
pprint(snailfish[0])