n,m = map(int,input().split())
c = 1
for i in range(1, m + 1):
    c = c * (n - m + i) // i
print(c%10007)    