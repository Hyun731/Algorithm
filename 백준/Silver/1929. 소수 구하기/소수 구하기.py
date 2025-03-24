import sys
n,m= map(int,sys.stdin.readline().split())
a = []
for i in range(1,m+1):
    a.append(i)
for i in range(n,m + 1):
    if i == 1:
        continue
    for j in range(2,int(i**0.5) + 1):
        if i % j == 0:
            break
    else:
        print(i)