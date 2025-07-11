import sys
limit_number = 15000
sys.setrecursionlimit(limit_number)
memo = {0 : 0, 1 : 1}
def fibo(n):
    if n == 0:
        return memo[0]
    elif n in memo:
        return memo[n]
    else:
        memo[n] = fibo(n-1) + fibo(n-2)
        return memo[n]

n = int(input())

print(fibo(n + 1)%10007)