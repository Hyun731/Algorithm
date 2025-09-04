import sys
n,m = map(int,input().split())
parent = [-1]*n
input = sys.stdin.readline
def union(a,b):
    fa = find(a)
    fb = find(b)
    if abs(parent[fa]) <= abs(parent[fb]):
        parent[fa] += parent[fb]
        parent[fb] = fa
    else:
        parent[fb] += parent[fa]
        parent[fa] = fb

def find(x):
    root = x
    while parent[root] >= 0:
        root = parent[root]
    while x != root:
        parent[x], x = root, parent[x]
    return root

for i in range(m):
    a, b = map(int, input().split())
    if find(a) == find(b):
        print(i + 1)
        break
    union(a,b)
else:
    print(0)