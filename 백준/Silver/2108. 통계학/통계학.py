import sys
from collections import Counter

input = sys.stdin.readline
n = int(input())
a = [int(input()) for _ in range(n)]
s_a = sorted(a)

print(int(round(sum(a) / n)))

print(s_a[n // 2])

count = Counter(a)
max_freq = max(count.values())
freq_list = [k for k, v in count.items() if v == max_freq]
freq_list.sort()
print(freq_list[1] if len(freq_list) > 1 else freq_list[0])

print(max(a) - min(a))