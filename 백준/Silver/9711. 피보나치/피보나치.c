#include <stdio.h>

unsigned long long f(int n, unsigned long long mod) {
    unsigned long long a = 0, b = 1, c;
    if (n == 0) return 0;
    for (int i = 2; i <= n; i++) {
        c = (a + b) % mod;
        a = b;
        b = c;
    }
    return b % mod;
}

int main() {
    int T;
    scanf("%d", &T);
    for (int i = 1; i <= T; i++) {
        int P;
        unsigned long long Q;
        scanf("%d %llu", &P, &Q);
        printf("Case #%d: %llu\n", i, f(P, Q));
    }
    return 0;
}