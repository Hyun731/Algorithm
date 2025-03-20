n = int(input())
sum = 0
for i in range(n):
    for j in range(n):
        if(3*i + 5*j == n):
            sum = i + j
            break
    if(3*i + 5*j == n):
            break
if(sum == 0):
    print(-1)
else:
    print(sum)