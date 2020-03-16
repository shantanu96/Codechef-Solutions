for _ in range(int(input())):
    p = int(input())
    if p > 2048:
        temp = p//2048
        rem = p%2048
        print(temp+bin(rem).count('1'))
    else:
        print(bin(p).count('1'))