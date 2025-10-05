n = int(input())
m = list(map(int,input().split()))
cnt = 0
ma = 0
for i in m:
    if i != 0:
        cnt += 1
    else:
        if cnt > ma:
            ma = cnt
        cnt = 0
print(max(ma,cnt))