n = int(input())
pair = int(input())
DFS = {i : [] for i in range(1,n + 1)}
for i in range(1,pair + 1):
    a,b = map(int,input().split())
    DFS[a].append(b)
    DFS[b].append(a)
visited = { i : False for i in range(1,n + 1)}
cnt = 0
def f(x):
    global cnt
    for node in DFS[x]:
        if not visited[node]:
            visited[node] = True
            cnt += 1
            f(node)
f(1)
if n == 1:
    print(0)
else:
    print(cnt - 1)