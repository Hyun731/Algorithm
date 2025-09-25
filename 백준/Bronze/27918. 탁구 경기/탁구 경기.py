n = int(input())
d = {'D' : 0,'P' : 0}
for i in range(n):
    d[input()] += 1
    if abs(d['D'] - d['P']) == 2:
        break
    
print(f"{d['D']}:{d['P']}")