#include <stdio.h>
int map[101][101], visited[101], n;
void dfs(int x) {
    visited[x] = 1;
    for (int i = 1; i <= n; i++)
        if (map[x][i] && !visited[i]) dfs(i);
}
int main() {
    int m, a, b, count = 0;
    scanf("%d %d", &n, &m);
    for (int i = 0; i < m; i++) {
        scanf("%d %d", &a, &b);
        map[a][b] = map[b][a] = 1;
    }
    dfs(1);
    for (int i = 2; i <= n; i++) if (visited[i]) count++;
    printf("%d\n", count);
    return 0;
}