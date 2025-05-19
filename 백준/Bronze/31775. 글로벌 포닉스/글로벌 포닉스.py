w = ['l','p','k']
a = input()
b = input()
c = input()
a = a[0]
b = b[0]
c = c[0]
if a != b and b != c and a != c:
    if a in w:
        w.remove(a)
        if b in w:
            w.remove(b)
            if c in w:
                print("GLOBAL")
            else:
                print("PONIX")
        else:
            print("PONIX")
    else:
        print("PONIX")
else:
        print("PONIX")