#include <stdio.h>
#include <math.h>

int main() {
    int n;
    scanf("%d", &n);

    int dp[n + 1];
    for (int i = 0; i <= n; i++) {
        dp[i] = i; 
    }

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j * j <= i; j++) {
            if (dp[i] > dp[i - j * j] + 1) {
                dp[i] = dp[i - j * j] + 1;
            }
        }
    }

    printf("%d\n", dp[n]);
    return 0;
}