#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

float check(float wid,float mid){
	if(mid > (wid / 2))
		return mid;
	else if (mid < (wid/2))
		return wid - mid;
	else
		return wid - mid;
}
float change(float num){
	if (num < 0)
		return num * -1;
	else
		return num;
}


int main(){
	float len[3][2] = {0,};
	float wid,m;
	scanf("%f",&wid);
	float mid = wid / 2;
	for(int i = 0; i < 3; i++){
		scanf("%f %f",&len[i][0],&len[i][1]);
	}
	mid = ((len[0][0] + len[0][1])) / 2; //빨간점 중앙 
	wid = check(wid,mid); //전체 길이 구하기 
	for(int i = 1; i < 3; i++){ //좌표수정 
		for(int j = 0; j < 2; j++){
			len[i][j] = change(len[i][j] - mid);
		}
	}
	if(len[1][0] != len[1][1]){
		mid = ((len[1][0] + len[1][1])) / 2; //파란점 중앙 
		wid = check(wid,mid); //전체 길이 구하기 
		for(int i = 2; i < 3; i++){ //좌표수정 
			for(int j = 0; j < 2; j++){
				len[i][j] = change(len[i][j] - mid);
			}
		}
	}
	mid = ((len[2][0] + len[2][1])) / 2; //파란점 중앙 
	wid = check(wid,mid); //전체 길이 구하기 
	printf("%.1f",wid);
}