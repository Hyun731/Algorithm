def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
def lcm(a, b):
    return a * b // gcd(a, b)

a,b = map(int,input().split())
c = b // a
p = []
for i in range(1,c//2 + 1):
    if c % i == 0:
        p.append(i)
p.append(c)
k = (p[0], p[len(p)-1])
for i in range(len(p)//2 + 1):
    if gcd(p[i],p[len(p) - i - 1]) == 1 and sum(k) > p[i] + p[len(p) - i - 1]:
        k = (p[i], p[len(p) - i - 1])
print(k[0] * a, k[1] * a)
