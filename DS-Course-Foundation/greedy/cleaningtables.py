for _ in range(int(input())):
    n,m = map(int,input().split())
    c = list(map(int,input().split()))
    tables = []
    count=0
    for i in range(m):
        if c[i] in tables:
            continue
        count+=1
        if len(tables)<n:
            tables.append(c[i])
            continue
        x=0
        temp = tables.copy()
       	#check which customer will order in the future
	#select only those customers that don't order in future
	#if all customers order in future select any one to be replaced
        for x in c[i+1:]:
            if len(temp) <= 1:
                break
            if x in temp:
                temp.remove(x)
        tables.append(c[i])
        tables.remove(temp[0])
    print(count)