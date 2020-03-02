for _ in range(int(input())):
    n,k = map(int,input().split())
    temp= list(input().split())
    ar = []
    for i in temp:
        if i=='H':
            ar.append(1)
        else:
            ar.append(0)
    flipcount = 0
    flag = False
    #start from last pos, iterate k times
    for i in range(n-1,n-k-1,-1):
        #if flipcount is odd flip the coin else don't
        if flipcount%2!=0:
            ar[i] = abs(ar[i]-1)
        if ar[i]==1:
            flipcount+=1
    #flip the remaining coins if flipcount even
    if(flipcount%2!=0):
        print(ar[:n-k].count(0))
    else:
        print(ar[:n-k].count(1))