for _ in range(int(input())):
    n = int(input())
    lst = list(map(int,input().split()))
    total=0
    for i in range(n-1):
        diff = abs(lst[i+1]-lst[i])-1
        if diff>-1:
            total+=diff
            
    print(total)