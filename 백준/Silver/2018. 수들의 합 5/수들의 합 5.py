n = int(input())
cnt = 0
for i in range(1,n + 1):
    if (n - i*(i-1)//2) % i == 0 and n - i*(i-1)//2 > 0:
        cnt += 1
print(cnt)