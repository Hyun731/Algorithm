k,n = map(int,input().split())
arr = []
for i in range(k):
    arr.append(int(input()))
low = 1
high = max(arr)
r = 0

while(low <= high):
    mid = (high+low)//2
    s = sum(i // mid for i in arr)
    if s >= n:
        r = mid
        low = mid + 1
    elif s//mid < n:
        high = mid - 1
print(r)    