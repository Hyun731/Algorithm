import sys

input = sys.stdin.readline

n, m = map(int, input().split())
num_name = {}
name_num = {}

for i in range(1, n + 1):
    name = input().strip()
    num_name[str(i)] = name
    name_num[name] = str(i)

for _ in range(m):
    q = input().strip()
    if q.isdigit():
        print(num_name[q])
    else:
        print(name_num[q])