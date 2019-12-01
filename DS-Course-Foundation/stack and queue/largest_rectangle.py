while True:
    tc = [int(x) for x in input().split()]
    n = tc[0]
    if n == 0:
        break
    tc.pop(0)
    htStack = []
    posStack = []
    maxArea,pos,tempH,tempPos=0,0,0,0
    
    def popIt():
        global tempH
        global tempPos
        global maxArea
        tempH = htStack.pop()
        tempPos = posStack.pop()
        area = tempH * (pos-tempPos)
        if area > maxArea:
            maxArea = area
   
    
    while pos < len(tc):
        ht = tc[pos]
        if len(htStack)==0 or ht > htStack[-1]:
            htStack.append(ht)
            posStack.append(pos)
        elif ht < htStack[-1]:
            while len(htStack) > 0 and ht < htStack[-1]:
                popIt()
            htStack.append(ht)
            posStack.append(tempPos)
            
        pos+=1
    while len(htStack) > 0:
        popIt()
        
    print(maxArea)
