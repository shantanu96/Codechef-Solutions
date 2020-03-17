for _ in range(int(input())):
    n,k = map(int,input().split())
    w = list(map(int,input().split()))
    w.sort()
    k = min(k,n-k)
    print(sum(w[k:])-sum(w[:k]))