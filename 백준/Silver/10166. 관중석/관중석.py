def gcd(a,b):
    if a % b == 0:
        return b
    return (gcd(b,a%b))
cnt = 0
room = [[0] * 2001 for _ in range(2001)]
n,m = map(int,input().split())
for i in range(n,m+1):
    for j in range(1,i+1):
        g = gcd(i,j)
        if(room[i//g][j//g] != 1):
            room[i//g][j//g] = 1
            cnt+=1
print(cnt)