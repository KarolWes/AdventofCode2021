import numpy as np

t = np.zeros((21,21))



f =open("tmp.txt", "r")
center = [5,5]
center_max = [10,10]
probe = 0
for line in f:
    if line[0] == '-' and line[1] == '-':
        small = np.zeros((11,11))
        #small *=-1
        small[5,5] = 2
    elif line != "\n":
        coordiantes = list(map(int, line.strip().split(',')))
        small[center[1]-coordiantes[1], center[0]+coordiantes[0]] = 1
    else:
        if probe == 0:
            probe +=1
            for i in range(len(small)):
                for j in range(len(small)):
                    if small[i,j] != -1:
                        t[center_max[1] - (center[1] - i), center_max[0] - (center[0] - j)] = small[i,j]
        else:
            res = np.isin(t, small)
        #
#print(small)
res = np.isin(t, [[1,0]])
print(1)