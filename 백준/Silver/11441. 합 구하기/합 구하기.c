#include <stdio.h>

int arr[100000];
int main() {
    int n;
    scanf("%d",&n);
    for(int i = 0; i < n; i++)
        scanf("%d",&arr[i]);
    int m,a,b,s;
    scanf("%d",&m);
    for(int i = 0; i < m; i++){
        scanf("%d %d",&a,&b);
        for(int j = a-1; j < b; j++){
            s += arr[j];
        }
        printf("%d\n",s);
        s = 0;
    }
}