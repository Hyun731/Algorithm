#include <stdio.h>

int main() {
    int N;
    scanf("%d", &N);

    int len = 1;       
    int start = 1;      
    int ans = 0;      

    while (start <= N) {
        int end = start * 10 - 1;     
        if (end > N) end = N;         
        ans += (end - start + 1) * len;
        start *= 10;                 
        len++;
    }

    printf("%d\n", ans);
    return 0;
}