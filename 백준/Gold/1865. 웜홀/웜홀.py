import sys
input = sys.stdin.read

def bellman_ford(n, edges):
    distance = [0] * (n + 1)

    for i in range(n):
        for u, v, w in edges:
            if distance[v] > distance[u] + w:
                distance[v] = distance[u] + w
                if i == n - 1:
                    return True
    return False

data = input().split()
t = int(data[0])
index = 1

results = []
for _ in range(t):
    n = int(data[index])
    m = int(data[index + 1])
    w = int(data[index + 2])
    index += 3

    edges = []

    for _ in range(m):
        s = int(data[index])
        e = int(data[index + 1])
        t_ = int(data[index + 2])
        edges.append((s, e, t_))
        edges.append((e, s, t_))
        index += 3

    for _ in range(w):
        s = int(data[index])
        e = int(data[index + 1])
        t_ = int(data[index + 2])
        edges.append((s, e, -t_))
        index += 3

    if bellman_ford(n, edges):
        results.append("YES")
    else:
        results.append("NO")

print('\n'.join(results))