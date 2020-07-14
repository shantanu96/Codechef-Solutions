for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    
    if n==1:
        if a==b:
            print(0)
        else:
            print(-1)
        continue
    unique = set(a).union(set(b))
    
    ca = {}
    cb = {}
    mn = 10**9
    xorcheck = 0
    for i in a:
        xorcheck ^= i
        if i not in ca:
            ca[i]=0
        ca[i]+=1
        if i < mn:
            mn = i
    for i in b:
        xorcheck ^= i
        if i not in cb:
            cb[i]=0
        cb[i]+=1
        if i < mn:
            mn = i
    
    if xorcheck:
        print(-1)
        continue
    
    for k,v in ca.items():
        if k in cb:
            dx = min(v,cb[k])
            ca[k] -= dx
            cb[k] -= dx
    
    A=[]
    B=[]
    
    for k,v in ca.items():
        for i in range(v//2):
            A.append(k)
    for k,v in cb.items():
        for i in range(v//2):
            B.append(k)
            
    if len(A)==len(B)==0:
        print(0)
        continue
    
    A.sort()
    B.sort(reverse=True)
    
    totalcost=0
    for i in range(len(A)):
        totalcost += min(2*mn,min(A[i],B[i]))
    
    print(totalcost)
        
        
    