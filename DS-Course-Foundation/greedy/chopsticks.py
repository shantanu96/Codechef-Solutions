n,d = map(int,input().split())
lst = []
for _ in range(n):
    lst.append(int(input()))
lst.sort()
count=0
i=0
while i<len(lst)-1:
    if lst[i+1]-lst[i] <= d:
        count+=1
        i+=2
    else:
        i+=1
        
print(count)