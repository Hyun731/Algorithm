n = int(input())
a = (8 + 7 * (n-1))
m = a % 12
y = 2024 + a//12
if m == 0:
    y -= 1
    m = 12
print(y,m)