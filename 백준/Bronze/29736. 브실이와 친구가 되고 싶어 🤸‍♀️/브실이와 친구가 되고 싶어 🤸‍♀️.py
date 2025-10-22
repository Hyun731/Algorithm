A, B = map(int, input().split())
K, X = map(int, input().split())

left = max(A, K - X)
right = min(B, K + X)

if right < left:
    print("IMPOSSIBLE")
else:
    print(right - left + 1)