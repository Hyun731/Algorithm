X, Y, Z = map(int, input().split())
U, V, W = map(int, input().split())

cost_A = (U // 100) * X
cost_B = (V // 50) * Y
cost_C = (W // 20) * Z

total = cost_A + cost_B + cost_C
print(total)