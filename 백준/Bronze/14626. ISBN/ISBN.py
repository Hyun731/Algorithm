a = list(input())
s = 0
star = 0

for i in range(len(a) - 1):
    if a[i] == "*":
        star = i
    else:
        if i % 2 == 0:
            s += int(a[i])*1
        else:
            s += int(a[i])*3
for i in range(10):
    total = s + i * (1 if star % 2 == 0 else 3)
    check = (10 - (total % 10)) % 10
    if check == int(a[-1]):
        print(i)
        break