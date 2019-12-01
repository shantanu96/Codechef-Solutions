c=0
while True:
    tc = input().strip()
    if tc[0] == '-':
        break
    c1=0
    c2=0
    for i in tc:
        if i == '{':
            c1+=1
        elif i == '}':
            if c1 > 0:
                c1-=1
            else:
                c2+=1
    opr= int(c1 / 2) + int(c2 / 2) + (2 * (c1 % 2))
    c+=1
    print(str(c)+". "+str(opr))