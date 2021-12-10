import math
import statistics as stat

f = open("input.txt", "r")
pos = list(map(int, f.readline().split(",")))

avg = sum(pos)/len(pos)
avg_l = math.floor(avg)
avg_h = math.ceil(avg)
m = stat.mode(pos)
med = stat.median(pos)
res_l = 0
for num in pos:
    test = abs(num-avg_l)+1
    res_l+=sum(range(test))
res_h = 0
for num in pos:
    test = abs(num-avg_h)+1
    res_h+= sum(range(test))
res_m = 0
for num in pos:
    test = abs(num - m)+1
    res_m += sum(range(test))
res_med = 0
for num in pos:
    test = abs(num - med)+1
    res_med += sum(range(int(test)))
print(min(res_l, res_h, res_m, res_med))
