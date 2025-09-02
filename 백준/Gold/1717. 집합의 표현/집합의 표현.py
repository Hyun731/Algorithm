import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [-1] * (n+1)

def find(x):
    if parent[x] < 0:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    fa = find(a)
    fb = find(b)
    if fa == fb:
        return
    if parent[fa] <= parent[fb]:
        parent[fa] += parent[fb]
        parent[fb] = fa
    else:
        parent[fb] += parent[fa]
        parent[fa] = fb

result = []
for _ in range(m):
    c, a, b = map(int, input().split())
    if c == 0:
        union(a, b)
    else:
        result.append("YES" if find(a) == find(b) else "NO")

print("\n".join(result))