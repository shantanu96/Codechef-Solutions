for _ in range(int(input())):
    n,m = map(int,input().split())
    x,y,s = map(int,input().split())
    x_riv = []
    y_riv = []
    if x>0:
        x_riv = list(map(int,input().split()))
    if y>0:
        y_riv = list(map(int,input().split()))
    
    xt,yt = 0,0
    xtot,ytot=0,0
    for i in x_riv:
        xtot += (i-xt-1)//s
        xt = i
    xtot += (n-xt)//s
    for i in y_riv:
        ytot += (i-yt-1)//s
        yt = i
    ytot += (m-yt)//s
    print(xtot*ytot)