A, B = map(int, input().split())
C, D = map(int, input().split())

th = A + C
ty = B + D

if th < ty:
    print("Hanyang Univ.")
elif th > ty:
    print("Yongdap")
else:
    print("Either")