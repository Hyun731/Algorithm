dir = {0 : 'N',90:'E',180:'S',270:'W'}
s = 0
for i in range(10):
    n = int(input())
    if n == 1:
        s += 90
    elif n == 2:
        s += 180
    else:
        s -= 90
print(dir[s%360])