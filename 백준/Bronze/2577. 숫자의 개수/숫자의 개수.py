a = int(input())
b = int(input())
c = int(input())
room = []
for i in range(10): room.append(0)
d = a*b*c

while d > 10:
    room[d % 10] += 1
    d = d // 10
room[d] += 1
print(*room,sep="\n")        