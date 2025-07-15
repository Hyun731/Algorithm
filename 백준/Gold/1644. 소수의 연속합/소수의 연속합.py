n = int(input())
arr = [True] * (n + 1)
prime = []
for i in range(2,n+1):
    if arr[i]:
        for j in range(i*2,n+1,i):
            arr[j] = False
        prime.append(i)

start = 0
end = 1
cnt = 0

while end <= len(prime):
    mid = sum(prime[start:end])
    if mid < n:
        end += 1
    elif mid > n:
        start += 1
    else:
        cnt += 1
        start += 1
print(cnt)