result = []
n_arr = []
m_arr = []

n = int(input())
n_arr = set(input().split())
m = int(input())
m_arr = list(input().split())

a = n_arr & set(m_arr)
for i in range(m):
    if m_arr[i] in a:
        result.append(1)
    else:
        result.append(0)
print(*result, sep="\n")