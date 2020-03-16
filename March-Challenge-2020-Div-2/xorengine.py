from sys import stdin, stdout

for _ in range(int(stdin.readline())):
    n,q = map(int,stdin.readline().split())
    a = list(map(int,stdin.readline().split()))
    e,o=0,0
    for i in range(n):
        if bin(a[i]).count('1')%2==0:
            e+=1
        else:
            o+=1
            
    for i in range(q):
        qry = int(stdin.readline())
        t1,t2 = e,o
        if bin(qry).count('1') % 2!=0:
            t1,t2=o,e
        stdout.write(str(t1)+" "+str(t2)+"\n")