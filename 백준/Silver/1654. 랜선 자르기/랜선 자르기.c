#include <stdio.h>
long long lines[10000];
int main() {
    int k, n;
    scanf("%d %d", &k, &n);
    for (int i = 0; i < k; i++) scanf("%lld", &lines[i]);
    long long l = 1, r = 0, mid, ans = 0;
    for (int i = 0; i < k; i++) if (lines[i] > r) r = lines[i];
    while (l <= r) {
        mid = (l + r) / 2;
        long long cnt = 0;
        for (int i = 0; i < k; i++) cnt += lines[i] / mid;
        if (cnt >= n) { ans = mid; l = mid + 1; }
        else r = mid - 1;
    }
    printf("%lld\n", ans);
    return 0;
}