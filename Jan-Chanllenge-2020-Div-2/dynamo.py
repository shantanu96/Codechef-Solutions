import sys
tc = int(input())
for i in range(tc):
    n = int(input())
    a = int(input())
    s = (2*(10**n))+a
    print(s)
    sys.stdout.flush()
    b = int(input())
    c = (10**n)-b
    print(c)
    sys.stdout.flush()
    d = int(input())
    e = (10**n)-d
    print(e)
    sys.stdout.flush()
    ans = int(input())
    if(ans==-1):
        break
