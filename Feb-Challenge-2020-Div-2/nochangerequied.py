for _ in range(int(input())):
    n,p = map(int,input().split())
    d = [int(x) for x in input().split()]
    flag = False
    for i in d:
        if p%i!=0:
            flag = True
            break
   
    if flag == False:
        print("NO")
        continue
    else:
        temp = [0]*len(d)
        minDiff = d[0]
        total=0
        i=len(d)-1
        while(total<=p):
            if(p%d[i]!=0):
                p1 = p - total
                div = int(p1/d[i])
                no = (div+1)*d[i]
                diff = no-d[i]
                if diff <= minDiff:
                    total+=no
                    temp[i] = div+1
                else:
                    total+=div*d[i]
                    temp[i] = div
            i-=1
        print("YES",end=" ")
        for i in temp:
            print(i,end=" ")
        print()
                    
