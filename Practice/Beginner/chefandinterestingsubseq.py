import math as m
for _ in range(int(input())):
    n,k = map(int,input().split())    
    a = list(map(int,input().split()))
    a = sorted(a)
    ar = a[:k]
    total = a.count(a[k-1])
    value = ar.count(ar[k-1])
    print(m.factorial(total)//(m.factorial(value)*m.factorial(total-value)))