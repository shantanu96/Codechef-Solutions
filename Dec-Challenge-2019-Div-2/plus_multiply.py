tc = int(input())
for i in range(tc):
    count = 0
    n = int(input())
    ar = [int(x) for x in input().split()]
    c0 = ar.count(0)
    if(c0 > 1):
        count += int((c0*(c0-1))/2)
        
    c2 = ar.count(2)
    if(c2 > 1):
        count += int((c2*(c2-1))/2)
        
    print(count)
