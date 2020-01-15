tc = int(input())
for i in range(tc):
    n = int(input())
    sub = dict.fromkeys(range(1,9), 0)
    for j in range(n):
        x,y = input().split()
        x = int(x)
        y = int(y)
        if x < 9:
            if y > sub[x]:
                sub[x] = y
    
    print(sum(sub.values()))
