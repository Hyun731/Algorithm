a, b = map(int, input().split())
cnt = 1

while b > a:
    if b % 10 == 1:
        b //= 10
        cnt += 1
    elif b % 2 == 0:
        b //= 2
        cnt += 1
    else:
        break

if b == a:
    print(cnt)
else:
    print(-1)