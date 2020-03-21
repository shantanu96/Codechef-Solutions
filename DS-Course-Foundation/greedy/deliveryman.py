total = 0
n,x,y = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
lst = [(a[x]-b[x],a[x],b[x]) for x in range(n)]
lst = sorted(lst,reverse=True)
total = 0
for i in lst:
    o = i
    if o[0]>0:
        if x>0:
            x-=1
            total+=o[1]
        else:
            y-=1
            total+=o[2]
    elif y>0:
        y-=1
        total+=o[2]
    else:
        x-=1
        total+=o[1]
print(total)