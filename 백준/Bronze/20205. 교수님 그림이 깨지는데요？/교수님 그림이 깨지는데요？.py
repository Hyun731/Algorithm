N, K = map(int, input().split())
bitmap = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):          
    expanded_row = []       
    for j in range(N):
        expanded_row += [bitmap[i][j]] * K  
        
    for _ in range(K):
        print(*expanded_row)