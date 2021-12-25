import numpy as np
f = open("input.txt", "r")
enhance = f.readline()
f.readline()


x = 0
tmp=[]
for line in f:
    tmp.append(list(line.strip()))
mapa = np.zeros((len(tmp)+x, len(tmp[0])+x))

center = [x//2,x//2]
for i in range(len(tmp)):
    for j in range(len(tmp[0])):
        if tmp[i][j] == '#':
            mapa[i+center[0],j+center[1]] = 1

for t in range(50):
    print(t)
    if t%2 == 0:
        n = 0
    else:
        n = 1
    new_test_mapa = np.pad(mapa, 2, constant_values=n)
    new_mapa = np.full((len(new_test_mapa), len(new_test_mapa[0])), n)
    for i in range(1, len(new_test_mapa)-1):
        for j in range(1, len(new_test_mapa)-1):
            test = new_test_mapa[i-1:i+2, j-1:j+2]
            val = ""
            for line in test:
                for el in line:
                    val+=str(int(el))
            code = int(val,2)
            
            if enhance[code]=='#':
                new_mapa[i,j] = 1
            else:
                new_mapa[i,j] = 0
    mapa = new_mapa[1:len(new_mapa)-1, 1:len(new_mapa[0])-1]

res = mapa.sum()
print(int(res))