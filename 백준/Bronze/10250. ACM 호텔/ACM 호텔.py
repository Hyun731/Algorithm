n = int(input())
result = []
for i in range(n):
    h,w,num = map(int,input().split())
    s_k = 0
    cnt = 0
    global k
    global j
    for k in range(1,w+1):
        for j in range(1,h+1):
           cnt += 1
           if num == cnt:
               break;
        if num == cnt:
            break 
    if k >= 10:
        s_k = k //10
        k %= 10
    print(j,s_k,k,sep="")
    