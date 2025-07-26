import sys
sys.setrecursionlimit(10**7)

def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
def get_divisors(n):
    divisors = []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors

memo = {}
def f(n):
    if isPrime(n):
        return 0
    if n in memo:
        return memo[n]
    res = float('inf')
    for d in get_divisors(n):
        part1 = d
        part2 = n // d
        val = max(f(part1), f(part2)) + 1
        if val < res:
            res = val
    memo[n] = res
    return res

n = int(input())
print(f(n))