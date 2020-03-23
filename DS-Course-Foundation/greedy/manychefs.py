for _ in range(int(input())):
    s = list(input())
    i=len(s)-1
    while i>=3:
        d = s[i]
        c = s[i-1]
        b = s[i-2]
        a = s[i-3]
        if (a=='C' or a=='?') and (b=='H' or b=='?') and (c=='E' or c=='?') and (d=='F' or d=='?'):
            if a=='?':
                s[i-3]='C'
            if b=='?':
                s[i-2]='H'
            if c=='?':
                s[i-1]='E'
            if d=='?':
                s[i]='F'
            i-=4
            continue
        else:
            if s[i]=='?':
                s[i]='A'
        i-=1
        
    for x in range(len(s)):
        if s[x]=='?':
            s[x]='A'
           
    print(''.join(s))
        
        
