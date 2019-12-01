n = int(input())
for i in range(n):
    exp = input()
    stk = []
    c = 0
    for i in  range(len(exp)):
        if len(stk)==0 and exp[i]==">":
            break
        
        if exp[i] == "<":
            stk.append(exp[i])
        elif len(stk)!=0 and exp[i] == ">":
            stk.pop()
        
        if len(stk)==0:
            c=i+1
        
        
    print(c)