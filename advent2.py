f = open("input.txt", "r")
h = 0
x = 0
a = 0
for line in f:
    command = line.split(" ");
    if command[0] == "forward":
        x += (int)(command[1])
        h+=a*(int)(command[1])
    elif command[0] == "down":
        a+= (int)(command[1])
    else:
        a-= (int)(command[1])
print(h*x)