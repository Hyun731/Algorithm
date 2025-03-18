n = int(input())
for i in range(n):
    temp = 0 
    a,b = map(int,input().split())
    sum = a*b
    while(a%b != 0):
        temp = a % b
        a = b
        b = temp
    print(sum//b)