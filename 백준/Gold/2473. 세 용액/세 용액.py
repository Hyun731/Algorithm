import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
a.sort()

min_abs = float('inf')
ans = (0, 0, 0)

for i in range(n - 2):
    left = i + 1
    right = n - 1

    while left < right:
        total = a[i] + a[left] + a[right]
        if total == 0:
            print(a[i], a[left], a[right])
            sys.exit()
        if abs(total) < min_abs:
            min_abs = abs(total)
            ans = (a[i], a[left], a[right])

        if total < 0:
            left += 1
        else:
            right -= 1

print(*ans)