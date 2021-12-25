w = 0
x = 0
y = 0
z = 0
i = 0
inp = []

def devaluate():
    global inp
    change = True
    i = -1
    while change:
        change = False
        inp[i] -=1
        if inp[i] == 0:
            inp[i] = 9
            i-=1
            change = True
    
    

def process(command):
    global w,x,y,z,i,inp
    if command[0] == "inp":
        if command[1] == 'w':
            w = inp[i]
        elif command[1] == 'x':
            x = inp[i]
        elif command[1] == 'y':
            y = inp[i]
        else:
            z = inp[i]
        i+=1
    elif command[0] == 'add':
        if command[1] == 'w':
            if command[2] == 'x':
                w += x
            elif command[2] == 'y':
                w+=y
            elif command[2] == 'z':
                w+=z
            else:
                w+=int(command[2])
        elif command[1] == 'x':
            if command[2] == 'w':
                x += w
            elif command[2] == 'y':
                x+=y
            elif command[2] == 'z':
                x+=z
            else:
                x+=int(command[2])
        elif command[1] == 'y':
            if command[2] == 'x':
                y += x
            elif command[2] == 'w':
                y+=w
            elif command[2] == 'z':
                y+=z
            else:
                y+=int(command[2])
        else:
            if command[2] == 'x':
                z += x
            elif command[2] == 'y':
                z+=y
            elif command[2] == 'w':
                z+=w
            else:
                z+=int(command[2])
    elif command[0] == 'mul':
        if command[1] == 'w':
            if command[2] == 'x':
                w *= x
            elif command[2] == 'y':
                w*=y
            elif command[2] == 'z':
                w*=z
            else:
                w*=int(command[2])
        elif command[1] == 'x':
            if command[2] == 'w':
                x *= w
            elif command[2] == 'y':
                x*=y
            elif command[2] == 'z':
                x*=z
            else:
                x*=int(command[2])
        elif command[1] == 'y':
            if command[2] == 'x':
                y *= x
            elif command[2] == 'w':
                y*=w
            elif command[2] == 'z':
                y*=z
            else:
                y*=int(command[2])
        else:
            if command[2] == 'x':
                z *= x
            elif command[2] == 'y':
                z*=y
            elif command[2] == 'w':
                z*=w
            else:
                z*=int(command[2])
    elif command[0] == 'div':
        if command[1] == 'w':
            if command[2] == 'x':
                w = w//x
            elif command[2] == 'y':
                w=w//y
            elif command[2] == 'z':
                w=w//z
            else:
                w=w//int(command[2])
        elif command[1] == 'x':
            if command[2] == 'w':
                x =x// w
            elif command[2] == 'y':
                x=x//y
            elif command[2] == 'z':
                x=x//z
            else:
                x=x//int(command[2])
        elif command[1] == 'y':
            if command[2] == 'x':
                y =y// x
            elif command[2] == 'w':
                y=y//w
            elif command[2] == 'z':
                y=y//z
            else:
                y=y//int(command[2])
        else:
            if command[2] == 'x':
                z =z// x
            elif command[2] == 'y':
                z=z//y
            elif command[2] == 'w':
                z=z//w
            else:
                z=z//int(command[2])
    elif command[0] == 'mod':
        if command[1] == 'w':
            if command[2] == 'x':
                w = w%x
            elif command[2] == 'y':
                w=w%y
            elif command[2] == 'z':
                w=w%z
            else:
                w=w%int(command[2])
        elif command[1] == 'x':
            if command[2] == 'w':
                x =x% w
            elif command[2] == 'y':
                x=x%y
            elif command[2] == 'z':
                x=x%z
            else:
                x=x%int(command[2])
        elif command[1] == 'y':
            if command[2] == 'x':
                y =y% x
            elif command[2] == 'w':
                y=y%w
            elif command[2] == 'z':
                y=y%z
            else:
                y=y%int(command[2])
        else:
            if command[2] == 'x':
                z =z% x
            elif command[2] == 'y':
                z=z%y
            elif command[2] == 'w':
                z=z%w
            else:
                z=z%int(command[2])
    elif command[0] == 'eql':
        if command[1] == 'w':
            if command[2] == 'x':
                w = 1 if w == x else 0
            elif command[2] == 'y':
                w = 1 if w == y else 0
            elif command[2] == 'z':
                w = 1 if w == z else 0
            else:
                w = 1 if w == int(command[2]) else 0
        elif command[1] == 'x':
            if command[2] == 'w':
                x = 1 if w == x else 0
            elif command[2] == 'y':
                x = 1 if x == y else 0
            elif command[2] == 'z':
                x = 1 if x == z else 0
            else:
                x = 1 if x == int(command[2]) else 0
        elif command[1] == 'y':
            if command[2] == 'x':
                y = 1 if y == x else 0
            elif command[2] == 'y':
                y = 1 if y == w else 0
            elif command[2] == 'z':
                y = 1 if y == z else 0
            else:
                y = 1 if y == int(command[2]) else 0
        else:
            if command[2] == 'x':
                z = 1 if z == x else 0
            elif command[2] == 'y':
                z = 1 if z == y else 0
            elif command[2] == 'w':
                z = 1 if z == w else 0
            else:
                z = 1 if z == int(command[2]) else 0
                
                
                
      
                
      
def calc(i, com):
    global z
    x = 0
    y = 0
    x = z
    x = x%26
    z = z//com[0]
    x+=com[1]
    if x != inp[i]:
        y = 26
    else:
        y = 1
    z*=y
    y = inp[i]+com[2]
    if x != inp[i]:
        z+=y
    
f = open("input.txt", "r")
com = []
for line in f:
    com.append(line.strip().split())
inp=[9,9,9,9,6,4,2,1,8,5,7,4,7,7]
steer = True

commands = [[1,13,3],[1,11,13],[1,15,9],[26,-6,12],
            [1,15,2],[26,-8,1],[26,-4,1],[1,15,13],
            [1,10,1],[1,11,6],[26,-11,2],[26,0,11],
            [26,-8,10],[26,-7,3]]

while steer:
    i = 0
    z = 0
    for line in commands:
        calc(i, line)
        i+=1
    if z == 0:
        for el in inp:
            print(el, end='')
        steer = False
    else:
        devaluate()
