#include <stdio.h>

long long cntzero(int n){
    long long cnt = 0;
    for (long long i = 5; i <= n; i *= 5) {
        cnt += n / i;
    }
    return cnt;
}

int main() {
    int n;
    long long m;
    scanf("%d",&n);
    for(int i = 0; i < n; i++){
        scanf("%lld",&m);
        printf("%lld\n",cntzero(m));
    }
}