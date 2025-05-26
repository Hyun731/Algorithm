n = int(input())
a,b = map(int,input().split())
if a//2 + b > n:
    print(n)
else:
    print(a//2 + b)