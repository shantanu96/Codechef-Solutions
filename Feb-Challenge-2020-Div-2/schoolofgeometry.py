tc = int(input())
for i in range(tc):
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    a = list(sorted(a))
    b = list(sorted(b))
    dsum = 0
    for j in range(n):
        if(a[j]<b[j]):
            dsum+=a[j]
        else:
            dsum+=b[j]
            
    print(dsum)
