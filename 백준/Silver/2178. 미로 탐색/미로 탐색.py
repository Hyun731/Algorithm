from collections import deque

n, m = map(int, input().split())

visited = [[False] * m for _ in range(n)]
arr = []
for i in range(n):
    arr.append(list(input()))

dist = [[0]*m for _ in range(n)]


def bfs(start):
    q = deque([start])
    c,d = start
    dist[c][d] = 1
    visited[c][d] = True
    while q:
        a,b = q.popleft()
        if a == n-1 and b == m-1:
            return dist[a][b]
        for i in {-1,1}:
            if 0 <= a+i < n and 0 <= b < m:
                if arr[a + i][b] == '1' and not visited[a + i][b]:
                    q.append((a + i, b))
                    visited[a + i][b] = True
                    dist[a+i][b] = dist[a][b] + 1
            if 0 <= a < n and 0 <= b + i < m:
                if arr[a][b + i] == '1' and not visited[a][b + i]:
                    q.append((a, b + i))
                    visited[a][b + i] = True
                    dist[a][b + i] = dist[a][b] + 1
print(bfs((0,0)))