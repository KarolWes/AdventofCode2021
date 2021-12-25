f = open("input.txt", "r")
mapa=[]
for line in f:
    mapa.append(list(line.strip()))
    
instance = 0
move = True
while move:
    new_mapa = []
    for line in mapa:
        new_mapa.append(line.copy())
    move = False
    for j in range(len(mapa)):
        i = 0
        while i < len(mapa[j]):
            if mapa[j][i] == '>':
                if i != len(mapa[j])-1:
                    if mapa[j][i+1] == '.':
                        new_mapa[j][i+1]='>'
                        new_mapa[j][i] = '.'
                        i+=1
                        move=True
                else:
                    if mapa[j][0] == '.':
                        new_mapa[j][0] = '>'
                        new_mapa[j][-1] = '.'
                        move = True
            i+=1
    mapa = []
    for line in new_mapa:
        mapa.append(line.copy())
    
    
    for i in range(len(mapa[0])):
        j = 0
        while j < len(mapa):
            if mapa[j][i] == 'v':
                if j!= len(mapa)-1:
                    if mapa[j+1][i] == '.':
                        new_mapa[j+1][i] = 'v'
                        new_mapa[j][i] = '.'
                        j+=1
                        move =True
                else:
                    if mapa[0][i] == '.':
                        new_mapa[0][i] = 'v'
                        new_mapa[-1][i] = '.'
                        move = True
            j+=1
    mapa = new_mapa
    instance+=1
    print(instance)
    
print(instance)