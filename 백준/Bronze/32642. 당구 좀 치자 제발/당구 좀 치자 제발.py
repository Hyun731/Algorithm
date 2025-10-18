n = int(input())
m = map(int,input().split())
num = 0
k = 0
for i in m:
    if i == 1:
        num += 1
        k += num
    else:
        num -= 1
        k += num
print(k)