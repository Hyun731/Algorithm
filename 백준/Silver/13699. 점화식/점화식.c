#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);

    long long t[36] = {0};
    t[0] = 1;
    t[1] = 1;
    t[2] = 2;
    t[3] = 5;

    if (n > 3) {
        for (int i = 4; i <= n; i++) {
            for (int j = 0; j < i; j++) {
                t[i] += t[j] * t[i - j - 1];
            }
        }
    }

    printf("%lld\n", t[n]);
    return 0;
}