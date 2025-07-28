import sys
input = sys.stdin.read

m = 100001
s = [0] * m
for i in range(2, m):
    if s[i] == 0:
        for j in range(i, m, i):
            if s[j] == 0:
                s[j] = i

def f(x):
    d = {}
    x = abs(x)
    while x > 1:
        p = s[x]
        d[p] = d.get(p, 0) + 1
        x //= p
    return d

z = input().split()
n = int(z[0])
z = z[1:]

a = {}
b = {}

x = int(z[0])
if x == 0:
    print("mint chocolate")
    exit()

for p, c in f(x).items():
    a[p] = a.get(p, 0) + c

for i in range(1, len(z), 2):
    o = z[i]
    x = int(z[i+1])
    if x == 0 and o == '*':
        print("mint chocolate")
        exit()

    d = f(x)
    if o == '*':
        for p, c in d.items():
            a[p] = a.get(p, 0) + c
    else:
        for p, c in d.items():
            b[p] = b.get(p, 0) + c

for p in b:
    if a.get(p, 0) < b[p]:
        print("toothpaste")
        break
else:
    print("mint chocolate")