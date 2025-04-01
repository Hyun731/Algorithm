def check(s):
    room = list(s)
    c = []
    for i in room:
        if i == '(' or i == '[':
            c.append(i)
        elif i == ')':
            if c and c[-1] == '(':
                c.pop()
            else:
                return 'no'
        elif i == ']':
            if c and c[-1] == '[':
                c.pop()
            else:
                return 'no'
    if not c:
        return 'yes'
    return 'no'
ans = []
s = input()
while s != '.':
    ans.append(check(s))
    s = input()
print(*ans,sep='\n')