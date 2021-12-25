speed = []
a_y = -1
target_x = [241,273]
target_y = [-97, -63]


vel_x = 500
while vel_x > 0:
    act = []
    for i in range(vel_x, 0, -1):
        test = sum(range(i, vel_x+1))
        if test in range(target_x[0], target_x[1]+1):
            act.append(vel_x)
            act.append(vel_x - i)
            print(vel_x)
            break
        if test > target_x[1]:
            break
    for i in range(0, vel_x+1):
        test = sum(range(i, vel_x+1))
        if test in range(target_x[0], target_x[1]+1):
            
            act.append(vel_x - i)
            print(vel_x)
            break
        if test < target_x[0]:
            break
    
    vel_x-=1
    if act != []:
        speed.append(act)



for el in speed:
    act = []
    for step in range(el[1], el[2]+1):
        vel_y = 30
        while True:
            test = sum(range((vel_y - step), vel_y+1))
            if test in range(target_y[0], target_y[1]+1):
                act.append(vel_y)
            if test < target_y[0]:
                break
            vel_y-=1
    if el[2] == el[0]:
        vel_y = 100
        step = el[2]+1
        test = sum(range((vel_y - step), vel_y+1))
        while test >= target_y[0]:
            while True:
                test = sum(range((vel_y - step), vel_y+1))
                if test in range(target_y[0], target_y[1]+1):
                    act.append(vel_y)
                if test < target_y[0]:
                    break
                step+=1
            vel_y-=1
            step = el[2]+1
            test = sum(range((vel_y - step), vel_y+1))
            
    el.append(act)

res = 0
for el in speed:
    res = max(res, sum(range(max(el[3])+1)))
print(res)
res = 0
for el in speed:
    res+= len(set(el[3]))
print(res)