n = int(input())
for i in range(n):
    eq = input()
    opr = []
    for i in eq:
        if i.isalpha():
            print(i,end="")
        elif i in ['+','-','*','^','/']:
            opr.append(i)

        if len(opr) != 0 and i == ')':
            n = opr.pop()
            print(n,end="")
    print()
