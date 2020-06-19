for _ in range(int(input())):
    n = int(input())
    grid = []
    for i in range(n):
        grid.append(input())
    count = 0
    
    X = [1]*n
    Y = [1]*n
    
    for i in range(n-1,-1,-1):
        for j in range(n-1,-1,-1):
            if grid[i][j]=='#':
                X[i] = 0
                Y[j] = 0
            else:
                if X[i]==Y[j]==1:
                    count+=1
    print(count)