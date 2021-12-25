f=open("input.txt", "r")
f2 =open("commands.txt","r")
mapa = []
for i in range(895):
    mapa.append(['.']*1311)
    
for line in f:
    point = list(map(int, line.strip().split(',')))
    mapa[point[1]][point[0]] = '#'

for line in f2:
    com = line.strip().split()
    com = com[2].split('=')
    div = int(com[1])
    if com[0] == 'y':            
        for i in range(1,int((len(mapa)+1)/2)):
            for j in range(len(mapa[0])):
                if mapa[div+i][j] == '#':
                    mapa[div-i][j] = '#'
        mapa = mapa[:div]
            
    else:
        for i in range(len(mapa)):
           for j in range(1, int((len(mapa[i])+1)/2)):
               if mapa[i][div+j] == '#':
                   mapa[i][div-j] = '#'
           mapa[i] = mapa[i][:div]
           
res = 0
for line in mapa:
    for el in line:
        
        if el =='#':
            print(el, end="")
            res+=1
        else:
            print(" ", end="")
    print()
print(res)