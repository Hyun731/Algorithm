n = int(input())
m = map(int,input().split())
num = 0
for i in m:
    if i <= n:
        num += i
    else:
        num += n
print(num)