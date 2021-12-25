import math
res = 0
s = []

def oper(t, num):
    global s
    op = s[-num:]
    s = s[:-num]
    if t == '000':
        tmp = sum(op)
        s.insert(0, tmp)
    elif t == '001':
        tmp = math.prod(op)
        s.insert(0, tmp)
    elif t == '010':
        s.insert(0, min(op))
    elif t == '011':
        s.insert(0,max(op))
    elif t == '101':
        if op[0] > op[1]:
            s.insert(0, 1)
        else:
            s.insert(0, 0)
    elif t == '110':
        if op[0] < op[1]:
            s.insert(0, 1)
        else:
            s.insert(0, 0)
    else:
        if op[0] == op[1]:
            s.insert(0, 1)
        else:
            s.insert(0, 0)

def parse(com, num_of_iter):
    if com != '0'*len(com):
        global res
        global s
        #print(s)
        v = com[:3]
        t = com[3:6]
        res+=int(v, 2)
        if t == '100':
            id = 0
            a = com[6:11]
            num = a[1:]
            while a[0] == '1':
                id+=1
                a = com[6+5*id:11+5*id]
                num = num + a[1:]
            n = int(num, 2)
            s.append(n)
            com = com[11+5*id:]
            if com != '0'*len(com):
                num_of_iter = parse(com, num_of_iter+1)
            else:
                return num_of_iter+1
        else:
            i = com[6]
            if i == '0':
                length = int(com[7:22], 2)
                act = len(s)
                parse(com[22:22+length], num_of_iter)
                num = len(s)-act
                oper(t, num)
                parse(com[22+length:], num_of_iter)
            else:
                num = int(com[7:18], 2)
                com = com[18:]
                parse(com, num_of_iter)
                oper(t, num)
    return num_of_iter
                                
            


f = open("input.txt","r")
line = f.readline().strip()
com = bin(int(line, 16))[2:].zfill(4*len(line))
parse(com, 0)
print("res: " + str(res))
print(s)
        
