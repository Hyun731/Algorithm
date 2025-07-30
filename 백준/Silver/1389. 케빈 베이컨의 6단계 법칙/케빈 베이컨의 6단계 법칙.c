#include <stdio.h>
#define INF 1000000
int dist[101][101];
int main() {
    int n, m, a, b;
    scanf("%d %d", &n, &m);
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= n; j++)
            dist[i][j] = (i == j) ? 0 : INF;
    while (m--) {
        scanf("%d %d", &a, &b);
        dist[a][b] = dist[b][a] = 1;
    }
    for (int k = 1; k <= n; k++)
        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= n; j++)
                if (dist[i][j] > dist[i][k] + dist[k][j])
                    dist[i][j] = dist[i][k] + dist[k][j];
    int min = INF, res = 0;
    for (int i = 1; i <= n; i++) {
        int sum = 0;
        for (int j = 1; j <= n; j++) sum += dist[i][j];
        if (sum < min) { min = sum; res = i; }
    }
    printf("%d\n", res);
    return 0;
}