a = int(input())

arr = []
result =[]
k = []

pr = []

for i in range(a):
    arr.append(int(input()))


no = 0
num = 0

for i in arr:
    if num <= i:
        while num <= i:
            k.append(num)
            pr.append("+")
            num += 1
        k.pop()
        pr.append("-")
    else:
        if k and k[-1] == i:
            k.pop()
            pr.append("-")
        else:
            print("NO")
            no = 1
            exit()
if not no:
    for i in pr[1:]:
      print(i)