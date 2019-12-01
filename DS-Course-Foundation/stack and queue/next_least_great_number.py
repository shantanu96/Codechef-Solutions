tc = int(input())
for i in range(tc):
    n = int(input())
    dig = [int(x) for x in input().split()]
    pivot = 0
    for i in range(len(dig)-2,-1,-1):
        if dig[i-1] < dig[i]:
            pivot = i
            break
        
    if pivot != 0:
        for i in range(pivot,len(dig)):
            if dig[i] < dig[pivot-1]: 
                dig[i-1],dig[pivot-1]=dig[pivot-1],dig[i-1]
                dig[pivot:]=sorted(dig[pivot:])
                break
            
    
    print("".join(map(str,dig)))