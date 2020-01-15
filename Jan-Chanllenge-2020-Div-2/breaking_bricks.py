tc = int(input())
for i in range(tc):
    x = [int(x) for x  in input().split()]
    s = x.pop(0)
    w1 = x[0]
    w2 = x[1]
    w3 = x[2]
    if w1+w2+w3 <= s:
        print("1")
    elif w1+w2 <= s:
        print("2")
    elif w2+w3 <= s:
        print("2")
    else:
        print("3")
