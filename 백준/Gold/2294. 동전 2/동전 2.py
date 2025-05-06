n,k = map(int,input().split())
c = []
for i in range(n):
    c.append(int(input()))
arr = [100000] * (k + 1)
arr[0] = 0

for coin in c:
    for i in range(coin, k + 1):
        arr[i] = min(arr[i], arr[i - coin] + 1)
        
if arr[k] == 100000:
    print(-1)
else:
    print(arr[k])