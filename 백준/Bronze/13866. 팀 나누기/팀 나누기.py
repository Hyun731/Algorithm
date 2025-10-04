a = list(map(int,input().split()))
a.sort()
x = a[0] + a[3]
y = a[1] + a[2]
print(abs(x-y))