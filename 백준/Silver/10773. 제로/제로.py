n = int(input())
room = []
for i in range(n):
    inp = int(input())
    if inp == 0:
        room.pop(len(room) - 1)
    else:
        room.append(inp)
print(sum(room))