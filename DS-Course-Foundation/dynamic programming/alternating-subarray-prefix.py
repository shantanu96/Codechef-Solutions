for _ in range(int(input())):
    n = int(input())
    ar = list(map(int,input().split()))
    nar = []
    for x in ar:
        if x<0:
            nar.append(-1)
        else:
            nar.append(1)
    dp = []
    count=1
    ele = nar[n-1]
    dp.append(count)
    ele *= -1
    for i in range(n-2,-1,-1):
        if ele == nar[i]:
            count += 1
        else:
            count = 1
            ele = nar[i]
        dp.append(count)
        ele *= -1
    dp.reverse()
    print(*dp)