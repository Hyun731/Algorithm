#include <stdio.h>
#define MOD 1000000007

long long dp[51];

int main() {
    int n;
    scanf("%d", &n);

    dp[0] = 1;
    if (n >= 1) dp[1] = 1;

    for (int i = 2; i <= n; i++) {
        dp[i] = (dp[i - 1] + dp[i - 2] + 1) % MOD;
    }

    printf("%lld\n", dp[n]);
    return 0;
}