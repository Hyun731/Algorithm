T = int(input())
scores = list(map(int, input().split()))

while len(scores) < 5:
    scores.append(0)
k, m, e, s, t = scores
if k > e:
    a = (k - e) * 508
else:
    a = (e - k) * 108
if m > s:
    b = (m - s) * 212
else:
    b = (s - m) * 305
c = t * 707

result = (a + b + c) * 4763
print(result)