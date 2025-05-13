from collections import deque

p = int(input())
for i in range(p):
    N,M = map(int, input().split())
    cnt = 0
    temp = list(map(int,input().split()))
    queue = deque()

    for i in range(N):
        queue.append((i,temp[i]))
    
    while queue:
        f = queue.popleft()
        if any(f[1] < q[1] for q in queue):
            queue.append(f)
        else:
            cnt += 1
            if f[0] == M: 
                print(cnt)
                break