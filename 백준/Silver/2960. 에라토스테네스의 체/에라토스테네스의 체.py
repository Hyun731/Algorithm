a = []
n,k = map(int,input().split())
pr = 0
k += 1
for i in range(n):
    a.append(i+1)
while(k != 0):
    p = min(a)
    a.remove(p)
    pr = p
    k -= 1
    for i in a:
        if i % p == 0:
            pr = i
            a.remove(i)
            k -= 1
            if k == 0:
                break
    if k == 0:
                break
print(pr)