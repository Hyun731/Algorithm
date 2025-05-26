room = []
for i in range(5):
    line = input()
    if "FBI" in line:
        room.append(i + 1)

if room:
    print(*room)
else:
    print("HE GOT AWAY!")