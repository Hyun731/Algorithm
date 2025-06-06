import sys
sys.setrecursionlimit(10**6)

def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)

def merge(A, p, q, r):
    global count, result, K
    tmp = [0] * (r - p + 2)
    i = p
    j = q + 1
    t = 1

    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp[t] = A[i]
            t += 1
            i += 1
        else:
            tmp[t] = A[j]
            t += 1
            j += 1

    while i <= q:
        tmp[t] = A[i]
        t += 1
        i += 1

    while j <= r:
        tmp[t] = A[j]
        t += 1
        j += 1

    i = p
    t = 1
    while i <= r:
        A[i] = tmp[t]
        count += 1
        if count == K:
            result = A[i]
        i += 1
        t += 1

N, K = map(int, input().split())
A = list(map(int, input().split()))

count = 0
result = -1

merge_sort(A, 0, N - 1)

print(result)
