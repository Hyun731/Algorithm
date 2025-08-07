#include <stdio.h>

int main() {
    int n, a, b, c;
    scanf("%d %d %d %d",&n,&a,&b,&c);
    long double high, low;
    high = a;
    if (b < high) high = b;
    if (c < high) high = c;
    low = 0.0L;
    for (int i = 0; i < 10000; i++) {
        long double mid = (high + low) / 2.0L;
        if((long long)(a/mid)*(long long)(b/mid)*(long long)(c/mid) >= n) low = mid;
        else high = mid;
    }
    printf("%.10Lf\n", low);
}