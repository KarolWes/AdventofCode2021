mapa = []
for i in range(1000):
    mapa.append([0]*1000)

f = open("input.txt", "r")
for line in f:
    tmp = line.split(" -> ")
    p1 = list(map(int, tmp[0].split(",")))
    p2 = list(map(int, tmp[1].split(",")))
    if p1[0] == p2[0]:
        for i in range(min(p1[1], p2[1]),max(p1[1], p2[1])+1):
            mapa[i][p1[0]] +=1
    elif p1[1] == p2[1]:
        for i in range(min(p1[0], p2[0]),max(p1[0], p2[0])+1):
            mapa[p1[1]][i] +=1
    else:
        lim =  max(p1[0], p2[0]) - min(p1[0], p2[0]) +1
        if (p1[0] - p2[0]) == (p1[1] -p2[1]):
            
            for i in range(lim):
                mapa[min(p1[1], p2[1]) + i][min(p1[0], p2[0]) + i] +=1
        else:
            for i in range(lim):
                mapa[min(p1[1], p2[1]) + i][max(p1[0], p2[0])-i] +=1
    
      
res = 0
for line in mapa:
    for el in line:
        if el > 1:
            res +=1
print(res)
