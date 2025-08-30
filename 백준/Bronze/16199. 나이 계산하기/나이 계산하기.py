y, m, d = map(int, input().split())   
y1, m1, d1 = map(int, input().split()) 
if (m1 > m) or (m1 == m and d1 >= d):
    print(y1 - y)
else:
    print(y1 - y - 1)
print(y1 - y + 1)
print(y1 - y)