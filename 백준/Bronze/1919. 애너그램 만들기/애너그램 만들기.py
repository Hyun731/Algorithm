# 입력 받기
a = input().strip()
b = input().strip()

# 알파벳 개수 저장할 배열 (a~z)
c_a = [0] * 26
c_b = [0] * 26

for ch in a:
    c_a[ord(ch) - ord('a')] += 1

for ch in b:
    c_b[ord(ch) - ord('a')] += 1

result = 0
for i in range(26):
    result += abs(c_a[i] - c_b[i])

print(result)