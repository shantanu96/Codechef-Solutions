for _ in range(int(input())):
    n = int(input())
    x=set()
    y=set()
    for i in range((4*n)-1):
        x1,y1 = map(int,input().split())
        if x1 not in x:
            x.add(x1)
        else:
            x.remove(x1)
        
        if y1 not in y:
            y.add(y1)
        else:
            y.remove(y1)
    
    print(*x,*y)