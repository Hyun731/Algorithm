#include <stdio.h>

int min(int a, int b) {
    return a < b ? a : b;
}

int main() {
    int N,M;
    int w_cnt = 0,b_cnt = 0;
    int a = 1000000;
    scanf("%d %d", &N,&M);
    char room[N][M];
    for(int i = 0; i < N; i++){
        scanf("%s",room[i]);
    }
    for(int i = 0; i <= (N-8); i++){
        for(int j = 0; j <= (M-8); j++){
            int w_cnt = 0;
            int b_cnt = 0;
            for (int x = 0; x < 8; x++) {
                for (int y = 0; y < 8; y++) {
                    if ((x+y)%2 == 0) {
                        if (room[i+x][j+y] != 'W') w_cnt++;
                        if (room[i+x][j+y] != 'B') b_cnt++;
                    } else { // 홀수칸
                        if (room[i+x][j+y] != 'B') w_cnt++;
                        if (room[i+x][j+y] != 'W') b_cnt++;
                    }
                }
            }
            a = min(a, min(w_cnt, b_cnt));
        }
    }
    printf("%d",a);
}