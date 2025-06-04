from collections import deque

n,m = map(int, input().split())

graph = {i : [] for i in range(1,n + 1)}
in_degree = [0] * (n + 1)
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    in_degree[b] += 1

o = list()

q = deque()

for i in range(1,len(in_degree)):
    if in_degree[i] == 0:
        q.append(i)
while q:
    node = q.popleft()
    o.append(node)
    for i in graph[node]:
        in_degree[i] -= 1
        if in_degree[i] == 0:
            q.append(i)
print(*o)