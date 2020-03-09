for _ in range(int(input())):
    n,m = map(int,input().split())
    f = list(map(int,input().split()))
    c = list(map(int,input().split()))
    dic = {}
    for i in range(n):
        if f[i] not in dic:
            dic[f[i]] = c[i]
        else:
            dic[f[i]] += c[i]
    print(min(dic.values()))