from itertools import permutations 
total = 0
for _ in range(int(input())):
    n = int(input())
    tbl = []
    for i in range(4):
        tbl.append([0,0,0,0])
    d = {'A':0,'B':1,'C':2,'D':3,'12':0,'3':1,'6':2,'9':3}
    for i in range(n):
        m,t = input().split()
        tbl[d[m]][d[t]] += 1
    comb = permutations([0,1,2,3])
    profit = -400
    for m in comb:
        temp = 0
        selected = []
        for t in range(4):
            selected.append(tbl[m[t]][t])
        selected.sort(reverse=True)
        price = 100
        for i in selected:
            if i>0:
                temp+=(i*price)
            else:
                temp-=100
            price-=25
        if temp>profit:
            profit=temp
    print(profit)
    total+=profit
print(total)