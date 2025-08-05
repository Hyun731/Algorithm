#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {
    char str[51];
    int cnt[26] = {0};
    scanf("%s", str);

    int len = strlen(str);

    for (int i = 0; i < len; i++) {
        cnt[str[i] - 'A']++;
    }

    int odd = 0;
    int odd_idx = -1;
    for (int i = 0; i < 26; i++) {
        if (cnt[i] % 2 == 1) {
            odd++;
            odd_idx = i;
        }
    }

    if (odd > 1) {
        printf("I'm Sorry Hansoo\n");
        return 0;
    }

    char half[51] = "";
    for (int i = 0; i < 26; i++) {
        for (int j = 0; j < cnt[i] / 2; j++) {
            int len_half = strlen(half);
            half[len_half] = i + 'A';
            half[len_half + 1] = '\0';
        }
    }

    printf("%s", half);
    if (odd == 1)
        printf("%c", odd_idx + 'A');
    for (int i = strlen(half) - 1; i >= 0; i--) {
        printf("%c", half[i]);
    }
    printf("\n");

    return 0;
}