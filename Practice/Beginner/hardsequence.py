for _ in range(int(input())):
    n = int(input())
    lst = [-1]*n
    curr = 0
    
    for i in range(n):
        lst[i] = curr
        if i==0:
            curr=0
            pass
        tList = lst[:i].copy()
        if curr in tList:
            lastO = len(tList)-tList[::-1].index(curr)-1
            curr = i-lastO
        else:
            curr = 0
    print(lst.count(lst[n-1]))