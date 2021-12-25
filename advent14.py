f=open("input.txt", "r")

template = list(f.readline().strip())
first = template[0]
last = template[-1]
f.readline()
s={}
count = {}
for line in f:
    com = line.strip().split()
    s[com[0]] = com[2]
source = {}
for i in range(1, len(template)):
    com = str(template[i-1]+template[i])
    if com in source.keys():
        source[com]+=1
    else:
        source[com] = 1
new_source = {}
for t in range(40):
    print(t)
    for el in source.keys():
        left = el[0]+s[el]
        right = s[el]+el[1]
        if left in new_source.keys():
            new_source[left]+=source[el]
        else:
            new_source[left]=source[el]
        if right in new_source.keys():
            new_source[right] +=source[el]
        else:
            new_source[right]= source[el]
    source = new_source
    new_source = {}
print(sum(source.values()))
for k in source.keys():
    if k[0] in count.keys():
        count[k[0]]+=source[k]
    else:
        count[k[0]] = source[k]
    if k[1] in count.keys():
        count[k[1]] +=source[k]
    else:
        count[k[1]] = source[k]
count[first]+=1
count[last]+=1
for k in count.keys():
    count[k]/=2
    


    # for i in range(1, len(template)):
    #     new_template.append(template[i-1])
    #     com = str(template[i-1]+template[i])
    #     new_template.append(s[com])
    # new_template.append(template[len(template)-1])
    # template = new_template
    # new_template = []
    
# print(len(template))
# for el in template:
#     if el in count.keys():
#         count[el]+=1
#     else:
#         count[el] = 1
print(max(count.values())-min(count.values()))