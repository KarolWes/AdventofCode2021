f = open("input.txt", "r")
a = [0]*12
n = 0
for line in f:
    n+=1
    for num in range(len(line)):
        if line[num] == "1":
            a[num] +=1

res_gamma = ""
res_epslion = ""
for num in a:
    if num*2 > n:
        res_gamma+="1"
        res_epslion+="0"
    else:
        res_gamma+="0"
        res_epslion+="1"
        
print(res_gamma)
print(res_epslion)
gamma = int(res_gamma, 2)
epsilon = int(res_epslion, 2)
res = gamma*epsilon
print(res)
f.close()


f = open("input.txt", "r")
tab = []
new_tab = []
x = 0
i = 0
for line in f:
    tab.append(line)
while len(tab) > 1:
    x = 0
    for line in tab:
        if line[i] == "1":
            x+=1
    if x*2 > len(tab)-1:
        for line in tab:
            if line[i] == "1":
                new_tab.append(line)
    else:
        for line in tab:
            if line[i] == "0":
                new_tab.append(line)
    tab = new_tab
    new_tab = []
    i+=1
ox = int(tab[0], 2)
print(ox)
f.close()

f = open("input.txt", "r")
tab = []
new_tab = []
x = 0
i = 0
for line in f:
    tab.append(line)
while len(tab) > 1:
    x = 0
    for line in tab:
        if line[i] == "1":
            x+=1
    if x*2 > len(tab)-1:
        for line in tab:
            if line[i] == "0":
                new_tab.append(line)
    else:
        for line in tab:
            if line[i] == "1":
                new_tab.append(line)
    tab = new_tab
    new_tab = []
    i+=1
co2 = int(tab[0], 2)
print(co2)
f.close()
print(co2*ox)     
            
            
            