import queue
player_1_pos = 8
player_2_pos = 7

player_1_points = 0
player_2_points = 0

player_1_wins = 0
player_2_wins = 0

dice = 1
throw = 0
k = 100

slot = 10
turn = 0


while player_1_points < 1000 and player_2_points < 1000:
    move = 0
    for _ in range(3):
        move += dice
        dice +=1
        dice = (dice-1)%k+1
        throw+=1
    if turn == 0:
        player_1_pos += move
        player_1_pos = (player_1_pos-1)%slot+1
        player_1_points += player_1_pos
    else:
        player_2_pos += move
        player_2_pos = (player_2_pos-1)%slot+1
        player_2_points += player_2_pos
    turn^=1
res = min(player_1_points, player_2_points)*throw
print(res)


q = queue.Queue()

player_1_pos = 4
player_2_pos = 8
player_1_points = 0
player_2_points = 0
lim = 21

l = [player_1_pos, player_1_points, player_2_pos, player_2_points, 1, 0]
q.put(l)
while not q.empty():
    l = q.get()
    if l[1] >= lim:
        player_1_wins+=l[4]
        print("p1: "+ str(player_1_wins))
    elif l[3] >= lim:
        player_2_wins+=l[4]
        print("p2: "+ str(player_2_wins))
    else:
        if l[5] == 0:
            l3=[(l[0]+2)%slot+1, l[1]+((l[0]+2)%slot+1),l[2],l[3],l[4], 1]
            l4=[(l[0]+3)%slot+1, l[1]+((l[0]+3)%slot+1),l[2],l[3],l[4]*3,1]
            l5=[(l[0]+4)%slot+1, l[1]+((l[0]+4)%slot+1),l[2],l[3],l[4]*6,1]
            l6=[(l[0]+5)%slot+1, l[1]+((l[0]+5)%slot+1),l[2],l[3],l[4]*7,1]
            l7=[(l[0]+6)%slot+1, l[1]+((l[0]+6)%slot+1),l[2],l[3],l[4]*6,1]
            l8=[(l[0]+7)%slot+1, l[1]+((l[0]+7)%slot+1),l[2],l[3],l[4]*3,1]
            l9=[(l[0]+8)%slot+1, l[1]+((l[0]+8)%slot+1),l[2],l[3],l[4],1]
            
        else:
           l3 = [l[0],l[1], (l[2]+2)%slot+1, l[3]+((l[2]+2)%slot+1), l[4], 0]
           l4 = [l[0],l[1], (l[2]+3)%slot+1, l[3]+((l[2]+3)%slot+1), l[4]*3, 0]
           l5 = [l[0],l[1], (l[2]+4)%slot+1, l[3]+((l[2]+4)%slot+1), l[4]*6, 0]
           l6 = [l[0],l[1], (l[2]+5)%slot+1, l[3]+((l[2]+5)%slot+1), l[4]*7, 0]
           l7 = [l[0],l[1], (l[2]+6)%slot+1, l[3]+((l[2]+6)%slot+1), l[4]*6, 0]
           l8 = [l[0],l[1], (l[2]+7)%slot+1, l[3]+((l[2]+7)%slot+1), l[4]*3, 0]
           l9 = [l[0],l[1], (l[2]+8)%slot+1, l[3]+((l[2]+8)%slot+1), l[4], 0]
        q.put(l3)
        q.put(l4)
        q.put(l5)
        q.put(l5)
        q.put(l7)
        q.put(l8)
        q.put(l9)
print(max(player_1_wins, player_2_wins))
        
                
                
            
            
            
            
            
            
            
        