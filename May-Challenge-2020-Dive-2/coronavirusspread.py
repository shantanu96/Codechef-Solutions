for _ in range(int(input())):
    n = int(input())
    x = list(map(int,input().split()))
    ar = []
    for i in range(0,n-1):
        ar.append(x[i+1]-x[i])
    count=1
    minc = 9999999
    maxc = 1
    for i in range(len(ar)):
        if ar[i]>2:
            if maxc < count:
                maxc = count
            if minc > count:
                minc = count
            count=1
            continue
        count+=1
    if maxc < count:
        maxc = count
    if minc > count:
        minc = count
    print(minc,maxc)