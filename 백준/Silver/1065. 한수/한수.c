#include <stdio.h>

int len(char *num){
    int l = 0;
    while(num[l] != '\0'){
        l++;
    }
    return l;
}

int main() {
    int n;
    int a;
    int f = 1;
    scanf("%d",&n);
    int cnt;
    if (n > 99)
        cnt = 99;
    else
        cnt = n;
    char num[4];
    if(n == 1000)
        n -= 1;
    for(int i = 100; i<=n; i++){
        a = i;
        num[3] = '\0';
        num[2] = (a % 10) + '0';
        a /= 10;
        num[1] = (a % 10) + '0';
        a /= 10;
        num[0] = (a % 10) + '0';
        for(int j = 0; j < len(num)-1; j++){
            if((num[j+1] - num[j]) == (num[j+2] - num[j+1])){
                f = 0;
                break;
            }
        }
        if(f == 0)
            cnt++;
        f = 1;
    }
    printf("%d",cnt);
}