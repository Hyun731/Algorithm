num = int(input())
a = list(map(int,input().split()))
m = max(a)
sum = 0
for i in a:
    sum += i/m*100
print(sum/num)