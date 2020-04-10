import math 
def primeFactors(n):
    l=[]
    while n % 2 == 0: 
        l.append(2)
        n = n / 2
    for i in range(3,int(math.sqrt(n))+1,2): 
        while n % i== 0: 
            l.append( i )
            n = n / i 
    if n > 2: 
        l.append(n)
    return len(l)

for _ in range(int(input())):
    x,k=map(int,input().split())
    a = primeFactors(x)
    if a >= k:
        print(1)
    else:
        print(0)