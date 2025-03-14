#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int D,K;
int check(int A,int B){
	int give[30] = {0,};
	give[0] = A;
	give[1] = B;
	int sum = 0,temp;
	for(int i = 2; i < D; i++){
		give[i] = give[i - 1] + give[i - 2];
	}
	if(give[D - 1] == K){
		return 1;
	}
	else
		return 0;
}

int main(){
	int out = 0,one,two;
	scanf("%d %d",&D,&K);
	for(int i = 1; i <= K; i++){
		for(int j = 1; j <= K; j++){
			out = check(i,j);
			if(out == 1){
				one = i;
				two = j;
				break;
			}
		}
		if(out == 1)
			break;
	}
	printf("%d\n%d",one,two);
}