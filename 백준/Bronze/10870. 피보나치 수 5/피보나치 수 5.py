n = int(input())
if n == 0:
    print(0)
else:
    a, b = 0, 1
    for c in range(n - 1):
        a, b = b, a + b
    d = max(a,b)
    print(d)