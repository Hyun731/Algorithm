#include <stdio.h>

int map[1001][1001], visited[1001];
int queue[10001], front = 0, rear = 0;
int n, m, v;

void dfs(int x) {
    visited[x] = 1;
    printf("%d ", x);
    for (int i = 1; i <= n; i++) {
        if (map[x][i] && !visited[i]) {
            dfs(i);
        }
    }
}

void bfs(int start) {
    for (int i = 1; i <= n; i++) visited[i] = 0;
    front = rear = 0;
    queue[rear++] = start;
    visited[start] = 1;

    while (front < rear) {
        int cur = queue[front++];
        printf("%d ", cur);
        for (int i = 1; i <= n; i++) {
            if (map[cur][i] && !visited[i]) {
                queue[rear++] = i;
                visited[i] = 1;
            }
        }
    }
}

int main() {
    int a, b;
    scanf("%d %d %d", &n, &m, &v);
    for (int i = 0; i < m; i++) {
        scanf("%d %d", &a, &b);
        map[a][b] = map[b][a] = 1; 
    }

    dfs(v);
    printf("\n");
    bfs(v);
    return 0;
}