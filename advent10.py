import queue
import statistics as stat
f = open("input.txt", "r")
fails = [0]*4
missing = []
scores =[]
for line in f:
    test = True
    opening = "([{<"
    closing = ")]}>"
    q = queue.LifoQueue()
    line = line.strip()
    for l in line.strip():
        if l in opening:
            q.put(l)
        else:
            if q.empty() == True:
                fails[closing.index(l)]+=1
                test = False
                break
                
            tmp = q.get()
            if abs(ord(l)-ord(tmp)) > 2:
                fails[closing.index(l)]+=1
                test = False
                break
    if test == True:  
        missing = []        
        while not(q.empty()):
            missing.append(q.get())
        res = 0
        for el in missing:
            res*=5
            res+=opening.index(el)+1
        scores.append(res)
            
res = 0
res+=fails[0]*3
res+=fails[1]*57
res+=fails[2]*1197
res+=fails[3]*25137
print(res)

scores = sorted(scores)
print(stat.median(scores))