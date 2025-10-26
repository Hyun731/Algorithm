temps = []

while True:
    t = float(input())
    if t == 999:
        break
    temps.append(t)

for i in range(1, len(temps)):
    diff = temps[i] - temps[i-1]
    print(f"{diff:.2f}")