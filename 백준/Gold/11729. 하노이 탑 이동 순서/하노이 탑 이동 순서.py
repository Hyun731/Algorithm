k = []
def hanoi(n,f,t,a):
    if n == 1:
        k.append((f,t))
        return 
    hanoi(n-1,f,a,t)
    k.append((f,t))
    hanoi(n-1,a,t,f)

n = int(input())
hanoi(n,1,3,2)
print(len(k))
for f,t in k:
    print(f,t)