for _ in range(int(input())):
    n,h,y1,y2,l = map(int,input().split())
    barriers = 0
    for _ in range(n):
        t,x = map(int,input().split())
        if l>0:
            if t==1 and x>=h-y1:
                barriers+=1
            elif t==2 and x<=y2:
                barriers+=1
            else:
                l-=1
                if l>0:
                    barriers+=1
    print(barriers)