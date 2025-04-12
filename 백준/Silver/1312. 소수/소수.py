a, b, n = map(int,input().split())

a %= b

for _ in range(n):
    a *= 10
    d = a // b
    a %= b
print(d)