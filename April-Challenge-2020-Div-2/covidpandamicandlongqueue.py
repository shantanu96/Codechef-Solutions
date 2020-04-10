for _ in range(int(input())):
    n = int(input())
    qu = list(map(int,input().split()))
    gap = 0
    temp = []
    if qu.count(1)==1:
        print("YES")
    else:
        flag = False
        for i in range(len(qu)):
            if flag == True and qu[i]==0:
                gap+=1
            elif qu[i]==1:
                if flag == True:
                    temp.append(gap)
                gap=0
                flag=True
        if len(temp)>0 and min(temp)>=5:
            print("YES")
        else:
            print("NO")