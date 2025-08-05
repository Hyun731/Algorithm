#include <stdio.h>

int main(){
    int dp[12];
    dp[1] = 1;
    dp[2] = 2;
    dp[3] = 4;
    int n = 0;
    int m = 0;
    scanf("%d",&n);
    for(int i = 0; i< n; i++){
      scanf("%d",&m);
      for(int j = 4; j <= m; j++){
          dp[j] = dp[j-1] + dp[j-2] + dp[j-3];
      }
      printf("%d\n",dp[m]);
    }
}