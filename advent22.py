import numpy as np

f=open("input.txt", "r")

def sumuj(ar):
    res = 0
    for el in ar:
        if el != 0:
            res+= bin(el).count("1")
    print(res)
    return res

# mapa = np.zeros((101,101,101))
# c=[]
# for line in f:
#     com = line.strip().split()
#     pos = com[1].split(',')
#     for i in range(3):
#         pos[i] = pos[i].split("..")
#         pos[i][0] = int(pos[i][0][2:])
#         pos[i][1] = int(pos[i][1])
#     if com[0] == 'on':
#         for i in range(pos[0][0]+50, pos[0][1]+51):
#             for j in range(pos[1][0]+50, pos[1][1]+51):
#                 for m in range(pos[2][0]+50, pos[2][1]+51):
#                     mapa[i,j,m] = 1
#     else:
#         for i in range(pos[0][0]+50, pos[0][1]+51):
#             for j in range(pos[1][0]+50, pos[1][1]+51):
#                 for m in range(pos[2][0]+50, pos[2][1]+51):
#                     mapa[i,j,m] = 0
#     c.append([com[0], pos])

# print(sum(mapa.flatten()))


c=[]
for line in f:
    com = line.strip().split()
    pos = com[1].split(',')
    for i in range(3):
        pos[i] = pos[i].split("..")
        pos[i][0] = int(pos[i][0][2:])
        pos[i][1] = int(pos[i][1])
    c.append([com[0], pos])

res = 0
for i in range(-100000,100001):
    mapa = np.zeros((200001, 6251), np.int32)
    for line in c:
        if i in range(line[1][0][0], line[1][0][1]+1):
            for j in range(line[1][1][0]+100000, line[1][1][1]+100001):
                for m in range(line[1][2][0]+100000, line[1][2][1]+100001):
                    index = m//32
                    pos = m%32
                    if line[0] == 'on':
                        mapa[j][index] = mapa[j][index]|(2**pos)
                    else:
                        mapa[j][index] = mapa[j][index]&(~(2**pos))
    res += sumuj(mapa.flatten())
                       
print(res)