n = int(input())
visited = set()
q = []
q.append((n, 0))
visited.add(n)
while q:
    n,cnt = q.pop(0)
    if n == 1:
        print(cnt)
        break
    if n % 3 == 0 and not n//3 in visited:
        q.append((n // 3, cnt + 1))
        visited.add(n//3)
    if n % 2 == 0 and not n//2 in visited:
        q.append((n // 2, cnt + 1))
        visited.add(n//2)
    if not n-1 in visited:
        q.append((n - 1, cnt + 1))
        visited.add(n-1)
