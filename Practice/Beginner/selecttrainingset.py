for _ in range(int(input())):
    dic = {}
    for _ in range(int(input())):
        w,s = input().split()
        if w not in dic:
            dic[w]={}
        if w+s not in dic[w]:
            dic[w][w+s] = 1
        else:
            dic[w][w+s] += 1
    total=0
    for i in dic.values():
        total += max(i.values())
    print(total)