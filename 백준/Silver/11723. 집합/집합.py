import sys

s = set()
n = int(sys.stdin.readline())
for i in range(n):
    a = list(sys.stdin.readline().split())
    if a[0] == "add":
        s.add(int(a[1]))
    elif a[0] == "remove":
        if int(a[1]) in s:
            s.remove(int(a[1]))
    elif a[0] == "check":
        print(1 if int(a[1]) in s else 0)
    elif a[0] == "toggle":
        if int(a[1]) in s:
            s.remove(int(a[1]))
        else:
            s.add(int(a[1]))
    elif a[0] == "all":
        s = set()
        for i in range(1, 21):
            s.add(i)
    elif a[0] == "empty":
        s = set()


