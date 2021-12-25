import queue
res = 100_000_000

def BFS(u):
    q = queue.Queue()
    q.put(u)
    global res
    while not(q.empty()):
        top = q.get()
        print(top)
        if mapa[top[0]+1][top[1]] != -1:
            if top[2] < res:
                q.put([top[0]+1, top[1], top[2]+mapa[top[0]+1][top[1]]])
        if mapa[top[0]][top[1]+1] != -1:
            if top[2] < res:
                q.put([top[0], top[1]+1, top[2]+mapa[top[0]][top[1]+1]])
        if top[0] == len(mapa)-2 and top[1] == len(mapa[0])-2:
            res = min(res, top[2])
            
            
            
def dijsktra():
    tab = []
    for i in range(len(mapa)):
        tab.append([0]*(len(mapa)))
    for i in range(len(mapa)):
        tab[0][i] = 10000
        tab[i][0] = 10000
        tab[-1][i] = 10000
        tab[i][-1] = 10000
    tab[1][1] = 0
    for i in range(1, len(mapa)-2):
        tab[i+1][1]=tab[i][1]+mapa[i+1][1]
        tab[1][i+1] = tab[1][i] + mapa[1][i+1]
    for i in range(1, len(mapa)-2):
        for j in range(1, len(mapa)-2):
            tab[i+1][j+1] = min(tab[i][j+1], tab[i+1][j])+mapa[i+1][j+1]
    print(tab[len(tab)-2][len(tab[0])-2])
    last = tab[len(tab)-2][len(tab[0])-2]
    new = last+1
    while new != last:
        last = new
        for i in range(1, len(mapa)-1):
            for j in range(1, len(mapa)-1):
                tab[i][j] = min(tab[i][j+1], tab[i+1][j], tab[i-1][j], tab[i][j-1])+mapa[i][j]
                tab[1][1] = 0
        print(tab[len(tab)-2][len(tab[0])-2])
        new = tab[len(tab)-2][len(tab[0])-2]
    
    
mapa = []

mapa.append([10000]*502)
for i in range(5):
    f = open("input.txt","r")
    for line in f:
        line = list(line.strip())
        l = [10000]
        for j in range(5):
            for el in line:
                l.append((int(el)+j+i-1)%9+1)
        l.append(10000)
        mapa.append(l)
    f.close()
mapa.append([10000]*502)
#BFS([1,1,0])
dijsktra()