a = []
for i in range(5):
    a.append(int(input()))
print(min(a[:3]) + min(a[3:]) - 50)