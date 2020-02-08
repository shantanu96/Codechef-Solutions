tc = int(input())
for i in range(tc):
    n,k = input().split()
    n,k = int(n),int(k)
    ar = [int(x) for x in input().split()]
    r = []
    for j in range(n):
        coins = 0
        a = ar.copy()
        #remove coins to get the no divisible by k upto jth position
        for x in range(j+1):
            rem = a[x]%k
            a[x] -= rem
            coins += rem
        #add the removed coins from j+1 to n pos such that all nos are div by k
        for y in range(j+1,n):
            d = int(a[y]/k)
            d+=1
            add = (d*k)-a[y]
            #if coins are less than required break else add as per requirement of bag
            if(add<=coins):
                a[y]+=add
                coins-=add
            else:
                break
        flag = True
        #check if all elements are div by k and then only add remaining coins to arr
        for l in range(n):
            if(a[l]%k!=0):
                flag = False
                break
        if(flag == True):
            r.append(coins)
        
    print(min(r))
            
