#include <stdio.h>

int main() {
    int n, k;
    int coin[10];
    scanf("%d %d", &n, &k);

    for (int i = 0; i < n; i++) {
        scanf("%d", &coin[i]);
    }

    int count = 0;

    for (int i = n - 1; i >= 0; i--) {
        if (coin[i] <= k) {
            count += k / coin[i]; 
            k %= coin[i];          
        }
    }

    printf("%d\n", count);
    return 0;
}