import sys
u = int(sys.stdin.readline())
for b in range(u):
    from collections import deque

    n,m = map(int, sys.stdin.readline().split())

    graph = {i : [] for i in range(1,n + 1)}
    in_degree = [0] * (n + 1)

    k = deque(map(int,sys.stdin.readline().split()))
    k.appendleft(0)

    for i in range(m):
        a,b = map(int,sys.stdin.readline().split())
        graph[a].append(b)
        in_degree[b] += 1
        
    w = int(sys.stdin.readline())

    dp = {}

    q = deque()

    for i in range(1,len(in_degree)):
        if in_degree[i] == 0:
            dp[i] = k[i]
            q.append(i)
    while q:
        node = q.popleft()
        for i in graph[node]:
            dp[i] = max(dp.get(i, 0), dp[node] + k[i])
            in_degree[i] -= 1
            if in_degree[i] == 0:
                q.append(i)
    print(dp[w])