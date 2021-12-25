res = 0
d = {}
p = []
double = ''

def DFS(u):
    global double
    global p
    p.append(u)
    if u == 'end':
        print(p)
        global res
        res+=1
        if p[-1] == double:
            double = ''
        p = p[:-1]
        return
    l = d.get(u)
    for el in l:
        if el.isupper():
            DFS(el)
        else:
            if not(el in p):
                DFS(el)
            else:
                if el != 'start' and el != 'end':
                    if double == '':
                        double = el
                        DFS(el)
    if p[-1] == double:
            double = ''
    p = p[:-1]
    return


f = open("input.txt", "r")

for line in f:
    path = line.strip().split("-")
    if path[0] in d.keys():
        d[path[0]].append(path[1])
    else:
        d[path[0]] = [path[1]]
    if path[1] != 'end' and path[0] != 'start' :
        if path[1] in d.keys():
            d[path[1]].append(path[0])
        else:
            d[path[1]] = [path[0]]

DFS('start')
print(res)