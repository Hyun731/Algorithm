dp = {}
n = int(input())
stair = []
for i in range(n):
    stair.append(int(input()))
if n == 1:
    print(stair[0])
elif n == 2:
    print(stair[0] + stair[1])
else:
    dp[0] = stair[0]
    dp[1] = stair[0] + stair[1]
    dp[2] = max(stair[0] + stair[2], stair[1] + stair[2])
    for i in range(3,n):
        dp[i] = max(dp[i - 2] + stair[i], dp[i-3] + stair[i-1] + stair[i])
    print(dp[n - 1])
