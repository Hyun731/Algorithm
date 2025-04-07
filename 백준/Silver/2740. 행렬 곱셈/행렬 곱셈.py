n,m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int,input().split())))
m,k = map(int, input().split())
b = []
for i in range(m):
    b.append(list(map(int,input().split())))

result = []
'''
1 2  -1 -2 0
3 4  0 0 3
5 6
'''

for i in range(n):
    x = [0] * k
    for j in range(m):
        for o in range(k):
            x[o] += a[i][j] * b[j][o]
    result.append(x)

for i in range(n):
    for j in range(k):
        print(result[i][j], end=" ")
    print()