n = int(input())

for i in range(n):
    score = 0
    cnt = 0
    a = input()
    for j in range(len(a)):
        if a[j] == 'O':
            cnt += 1
            score += cnt
        elif a[j] == 'X':
            cnt = 0
    print(score)
           
            