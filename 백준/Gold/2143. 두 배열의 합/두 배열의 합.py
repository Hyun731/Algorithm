import sys
from collections import Counter

input = sys.stdin.readline


T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

sumA = []
for i in range(n):
    temp = 0
    for j in range(i, n):
        temp += A[j]
        sumA.append(temp)

sumB = []
for i in range(m + 1):
    temp = 0
    for j in range(i, m):
        temp += B[j]
        sumB.append(temp)

counterB = Counter(sumB)

result = 0
for i in sumA:
    result += counterB[T - i]

print(result)