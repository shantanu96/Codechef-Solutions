n = -1
while n != 0:
    n = int(input())
    order = [int(x) for x in input().split()]
    need = 1
    lane = []
    success = True
    for i in range(n):
        while len(lane)!=0 and lane[-1]==need:
            need+=1
            lane.pop()
        
        if order[i]==need:
            need+=1
        elif len(lane)!=0 and lane[-1]<order[i]:
            success = False
            break
        else:
            lane.append(order[i])
            
    if success == True:
        print("yes")
    else:
        print("no")