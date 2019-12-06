#topcoder
def findDivisors(n):
    divisors = []
    i=2
    while(i*i<=n):
        if n%i==0:
            divisors.append(i)
            divisors.append(int(n/i))
        i+=1
    return divisors
        
def findOpr(n,m):
    valuesDic = dict.fromkeys(range(m+1), -1)
    qu = []
    qu.append(n)
    valuesDic[n]=0
    while len(qu) != 0:
        value = qu[0]
        qu.pop(0)
        if value == m:
            break
        for i in findDivisors(value):
            pathValue = value + i
            if((pathValue <= m) and (valuesDic[pathValue]==-1)):
                qu.append(pathValue)
                valuesDic[pathValue] = valuesDic[value] + 1
    return valuesDic[m]
    
print(findOpr(4,24))
print(findOpr(8748,83462))
