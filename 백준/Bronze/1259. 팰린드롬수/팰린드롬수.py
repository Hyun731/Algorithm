a = 1
while(1):
    a = list(str(input()))
    b = list(reversed(a)) 
    if '0' in a and len(a) == 1:
        break
    elif a == b:
        print("yes")
    else:
        print("no")