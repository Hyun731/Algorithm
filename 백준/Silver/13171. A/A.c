#include <stdio.h>

long long power(long a, long x) {
    long long result = 1;
    a %= 1000000007;
    while (x > 0) {
        if (x % 2 == 1) {
            result = (result * a) % 1000000007;
        }
        a = (a * a) % 1000000007;
        x /= 2;
    }
    return result;
}

int main() {
    long long A, X;
    scanf("%lld %lld", &A, &X);
    printf("%lld\n", power(A, X));
    return 0;
}