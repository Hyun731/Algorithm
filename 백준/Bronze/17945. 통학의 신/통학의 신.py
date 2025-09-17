import math

a, b = map(int,input().split())
c = math.sqrt(a**2-b)
d = sorted(set([-a + c,-a-c]))
for i in d:
    print(int(i),end=" ")