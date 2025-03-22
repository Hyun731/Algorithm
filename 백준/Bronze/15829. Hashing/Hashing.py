l = int(input())
room = list(input())
cnt = 0
sum = 0
for i in room:
    sum += (ord(i)-96)*(31**cnt)
    cnt+=1
print(sum)