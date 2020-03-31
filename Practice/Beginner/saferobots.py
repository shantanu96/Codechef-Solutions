import math
for _ in range(int(input())):
    s = input()
    sa,sb = map(int,input().split())
    ai = s.index('A')
    bi = s.index('B')
    e = bi-ai
    if e%(sa+sb)==0:
        print('unsafe')
    else:
        print('safe')