for _ in range(int(input())):
    n = int(input())
    if n==1:
        print("1")
        print("1 1")
    elif n==2:
        print("1")
        print("2 1 2")
    elif n==3:
        print("1")
        print("3 1 2 3")
    else:
        print(n//2)
        print("3 1 2 3")
        for i in range(4,n+1,2):
            if i==n:
                print("1",i)
            else:
                print("2",i,i+1)