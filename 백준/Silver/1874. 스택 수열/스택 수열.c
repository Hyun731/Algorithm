#include <stdio.h>

int arr[100001];
char c[200002];
int a[100001];
int top = 0;
int c_num = 0;

void push(int n) {
    arr[top++] = n;
    c[c_num++] = '+';
}

void pop() {
    top--;
    c[c_num++] = '-';
}

int main() {
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) 
        scanf("%d", &a[i]);

    int cnt = 0;
    for (int j = 1; j <= n; j++) {
        push(j);
        while (top > 0 && arr[top-1] == a[cnt]) {
            pop();
            cnt++;
        }
    }

    if (cnt != n) {
        printf("NO\n");
    }
    else{
        for(int i = 0; i < c_num; i++){
            printf("%c\n",c[i]);
        }
    }
}