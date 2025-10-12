n = int(input())
a = list(map(int,input().split()))
b = sum(a) + (n-1)*8
print(b//24,b%24)