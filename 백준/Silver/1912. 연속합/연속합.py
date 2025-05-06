n = int(input())
arr = list(map(int,input().split()))

store = [-1001]*100000
for i in range(len(arr)):
    if i == 0: store[i] = arr[i]
    else:
        store[i] = max(store[i-1] + arr[i],arr[i])
print(max(store))