n = int(input())
sum = 1
cnt = 0
for i in range(1,n+1):
    sum *= i
while((sum % 10) == 0):
    cnt += 1
    sum //= 10
print(cnt)