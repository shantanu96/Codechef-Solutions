for _ in range(int(input())):
    n1,n2,m = map(int,input().split())
    temp = min(n1,n2)
    res = min(temp,(m*(m+1))//2)
    print((n1-res)+(n2-res))