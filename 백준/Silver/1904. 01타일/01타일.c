#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);

    if (n == 1){
        printf("1\n"); 
        return 0; 
    }
    if (n == 2) {
        printf("2\n"); 
        return 0; 
    }

    int a = 1, b = 2;
    for (int i = 3; i <= n; i++) {
        int c = (a + b) % 15746;
        a = b;
        b = c;
    }
    printf("%d\n", b);
    return 0;
}