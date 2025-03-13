a = []
for i in range(26):
    a.append(-1)
n = input()
for j in n:
    a[ord(j) - 97] = n.index(j)
print(*a)