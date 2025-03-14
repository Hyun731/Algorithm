n = int(input())
S,M,L,XL,XXL,XXXL = map(int,input().split())
T, P = map(int,input().split())
cnt = 0

for i in S,M,L,XL,XXL,XXXL:
    if i <= T and i != 0:
        cnt+=1
    elif i % T == 0 and i != 0:
        cnt += (i//T)
    elif i > T and i != 0:
        cnt += (i // T) + 1
print(cnt)
print(n//P,n%P)