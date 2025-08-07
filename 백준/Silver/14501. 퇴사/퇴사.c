#include <stdio.h>
int m(int a,int b){
    return a > b ? a : b;
}
int main() {
    int dp[17] = {0,};
    int t[16] = {0,};
    int p[16] = {0,};
    int n;
    scanf("%d",&n);
    for(int i = 1; i <= n; i++){
        scanf("%d %d",&t[i],&p[i]);
    }
    for(int i = 1; i <= n+1; i++){
        dp[i + 1] = m(dp[i+1],dp[i]);
        if (i + t[i] <= n + 1)
            dp[i + t[i]] = m(dp[i+t[i]],dp[i]+p[i]);
    }
    printf("%d",dp[n + 1]);
}