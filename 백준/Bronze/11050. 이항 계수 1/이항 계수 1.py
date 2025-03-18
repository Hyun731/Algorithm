n,k = map(int,input().split())
def fac(a):
    if a == 0 or a == 1:
        return 1
    else:
        return a *fac(a-1)
print(int(fac(n)/(fac(k)*fac(n-k))))