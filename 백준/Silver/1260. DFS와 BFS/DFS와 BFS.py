n ,pair,v = map(int,input().split())
graph = {i : [] for i in range(1,n + 1)}
for i in range(1,pair + 1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in graph:
    graph[i].sort()
visited = { i : False for i in range(1,n + 1)}
sequence = []
def f(x):
    visited[x] = True
    sequence.append(x)
    for node in graph[x]:
        if not visited[node]:
            f(node)
f(v)
print(*sequence)
from collections import deque
visited = { i : False for i in range(1,n + 1)}
sequence = []
queue = deque([v])
visited[v] = True
while queue:
    node = queue.popleft()
    sequence.append(node)
    for vertex in graph[node]:
        if not visited[vertex]:
            visited[vertex] = True
            queue.append(vertex)
print(*sequence)