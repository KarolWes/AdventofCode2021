import sys

def sumuj(b):
    suma = 0
    for i in range(5):
        for j in range(5):
            if b[i][j] != -1:
                suma += int(b[i][j])
    suma *= int(n)
    print(suma)
    
    
f = open("input.txt", "r")
tmp = f.readline()
nums = tmp.split(',')
boards = []
newboard =[]
b = []

for line in f:
    if len(line) > 5:
        b.append(line.split())
        if len(b) == 5:
            boards.append(b)
            b = []

for n in nums:
    newboard = []
    for i in range(len(boards)):
        for j in range(5):
            for m in range(5):
                if boards[i][j][m] == n:
                    boards[i][j][m] = -1
    for b in boards:
        todelete = False
        for line in b:
            if line == [-1, -1, -1, -1, -1]:
                sumuj(b)
                todelete = True
                break
        for i in range(5):
            test = True
            for j in range(5):
                test = test and (b[j][i] == -1)
            if test:
                sumuj(b)
                todelete = True
                break
        if not(todelete):
            newboard.append(b)
    boards = newboard