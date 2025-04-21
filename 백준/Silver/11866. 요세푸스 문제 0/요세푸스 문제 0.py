n,m = map(int, input().split())
queue = []
for i in range(1,n+1):
    queue.append(i)
result = []
i = 1
while(queue):
    if i == m:
        result.append(queue.pop(0))
        i = 1
    else:
        queue.append(queue.pop(0))
        i += 1
print("<",end="")
print(*result,sep=", ",end="")
print(">")
