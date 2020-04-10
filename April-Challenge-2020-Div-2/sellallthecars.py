for _ in range(int(input())):
        n = int(input())
        l = [int(i) for i in input().split()]
        l.sort(reverse=True)
        profit = 0
        for i in range(0,n):
            if l[i] == 0:
                break
            else:
                if l[i]-i<0:
                    pass
                else:
                    profit = profit + l[i] - i
                    profit = profit% 1000000007
        print(profit% 1000000007)
