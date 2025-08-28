S = input().strip()  
count = [0] * 26     

for char in S:
    index = ord(char) - ord('a')  
    count[index] += 1

print(*count)