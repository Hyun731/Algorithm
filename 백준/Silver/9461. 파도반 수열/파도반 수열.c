#include <stdio.h>

int main(){
    long long dp[101];
    dp[1] = 1;
    dp[2] = 1;
    dp[3] = 1;
    dp[4] = 2;
    dp[5] = 2;
    int n = 0;
    int m = 0;
    scanf("%d",&n);
    for(int i = 0; i< n; i++){
      scanf("%d",&m);
      for(int j = 6; j <= m; j++){
          dp[j] = dp[j-1] + dp[j-5];
      }
      printf("%lld\n",dp[m]);
    }
}