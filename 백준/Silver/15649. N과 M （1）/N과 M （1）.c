#include <stdio.h>
#include <stdbool.h>

int N, M;
int arr[9];           
bool visited[9];      

void dfs(int depth) {
    if (depth == M) { 
        for (int i = 0; i < M; i++)
            printf("%d ", arr[i]);
        printf("\n");
        return;
    }
    for (int i = 1; i <= N; i++) {
        if (visited[i]) continue;  
        visited[i] = true;
        arr[depth] = i;             
        dfs(depth + 1);              
        visited[i] = false;         
    }
}

int main() {
    scanf("%d %d", &N, &M);
    dfs(0);
    return 0;
}