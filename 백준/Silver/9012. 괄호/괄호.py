def check(s):
    room = list(s)
    c = []
    for i in room:
        if i == '(':
            c.append(i)
        elif i == ')':
            if c:
                c.pop(len(c) - 1)
            else:
                return 'NO'
    if not c:
        return 'YES'
    return 'NO'     
    
n = int(input())
ans = []
for _ in range(n):
    s = input()
    ans.append(check(s))
print(*ans,sep='\n')