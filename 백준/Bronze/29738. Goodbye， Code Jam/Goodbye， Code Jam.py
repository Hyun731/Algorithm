t = int(input())

for case in range(1, t + 1):
    n = int(input())
    if n > 4500:
        result = "Round 1"
    elif n > 1000:
        result = "Round 2"
    elif n > 25:
        result = "Round 3"
    else:
        result = "World Finals"
    
    print(f"Case #{case}: {result}")