A, B = map(int, input().split())
C = int(input())

total = A + B
price = 2 * C

if total >= price:
    print(total - price)
else:
    print(total)