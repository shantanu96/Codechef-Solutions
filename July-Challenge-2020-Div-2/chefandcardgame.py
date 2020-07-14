for _ in range(int(input())):
    n = int(input())
    chef=morty=0
    for i in range(n):
        a,b = map(int,input().split())
        c=m=0
        while a>0:
            temp=a%10
            c+=temp
            a = a//10
        while b>0:
            temp=b%10
            m+=temp
            b = b//10
            
        if c>m:
            chef+=1
        elif m>c:
            morty+=1
        else:
            chef+=1
            morty+=1
    if chef>morty:
        print(0,chef)
    elif morty>chef:
        print(1,morty)
    else:
        print(2,chef)