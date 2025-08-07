#include <stdio.h>

int main() {
    int n, m;
    char board[51][51];

    scanf("%d %d", &n, &m);
    for (int i = 0; i < n; i++) {
        scanf("%s", board[i]);
    }

    int max = 1;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            for (int d = 1; i + d < n && j + d < m; d++) {
                if (board[i][j] == board[i][j + d] &&
                    board[i][j] == board[i + d][j] &&
                    board[i][j] == board[i + d][j + d]) {
                    int area = (d + 1) * (d + 1);
                    if (area > max)
                        max = area;
                }
            }
        }
    }

    printf("%d\n", max);
    return 0;
}