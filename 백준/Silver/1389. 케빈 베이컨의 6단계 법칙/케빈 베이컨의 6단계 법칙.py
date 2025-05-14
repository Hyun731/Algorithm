from collections import deque
n ,pair = map(int,input().split())
graph = {i : [] for i in range(1,n + 1)}
for i in range(1,pair + 1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

result = []
def a(i):
    visited = { i : False for i in range(1,n + 1)}
    dp = [0]*(n + 1)
    queue = deque([i])
    visited[i] = True
    while queue:
        node = queue.popleft()
        for vertex in graph[node]:
            if not visited[vertex]:
                visited[vertex] = True
                dp[vertex] = dp[node] + 1
                queue.append(vertex)
    return sum(dp)

mi = 99999999999;
person = 0
for i in range(1,n+1):
    t = a(i)
    if mi > t:
        mi = t
        person = i
print(person)