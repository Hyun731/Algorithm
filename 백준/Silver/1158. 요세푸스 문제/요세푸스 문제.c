#include <stdio.h>

int main() {
    int n, k;
    scanf("%d %d", &n, &k);

    int a[5001] = {0};
    for (int i = 0; i < n; i++) {
        a[i] = i + 1;
    }

    int idx = 0;
    int cnt = 0;
    int r = 0;

    printf("<");
    while (r < n) {
        if (a[idx] != 0) {
            cnt++;
            if (cnt == k) {
                if (r == n - 1)
                    printf("%d", a[idx]);
                else
                    printf("%d, ", a[idx]);
                a[idx] = 0;
                cnt = 0;
                r++;
            }
        }
        idx = (idx + 1) % n;
    }
    printf(">\n");
    return 0;
}