#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int gcd(int a,int b){
	if(a % b == 0)
		return b;
	else
		gcd(b,a%b);
}
int room[2001][2001];

int main(){
	int cnt = 0;
	int D1,D2,g;
	scanf("%d %d", &D1, &D2);
	for(int i = D1; i <= D2; i++){
		for(int j = 1; j <= i; j++){
			g = gcd(i,j);
			if(room[i/g][j/g] != 1){
				room[i/g][j/g] = 1;
				cnt++;
			}
		}
	}
	printf("%d",cnt);
}