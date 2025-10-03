n = input()

if n[0]=='"' and n[-1]=='"' and len(n) > 2:
    print(n[1:-1])
else:
    print("CE")