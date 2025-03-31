def binary_search(arr, s_data):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < s_data:
            low = mid + 1
        elif arr[mid] > s_data:
            high = mid - 1
        else:
            return mid  
    return -1  

n = int(input())
n_arr = list(map(int, input().split()))
m = int(input())
m_arr = list(map(int, input().split()))

n_arr.sort()

result = {}

for num in n_arr:
    if num in result:
        result[num] += 1
    else:
        result[num] = 1

for i in m_arr:
    print(result.get(i, 0), end=" ")
