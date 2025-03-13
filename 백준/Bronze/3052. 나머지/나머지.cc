#include <stdio.h>

int main(){
    int room[10];
    int n[10] = {-1,};
    bool is_not = true;
    int cnt = 0;
    for (int i = 0; i < 10; i++){
        scanf("%d",&room[i]);
        room[i] %= 42;
    }

    for (int i = 0; i < 10; i++)
    {
        for (int j = 0; j < 10; j++)
        {
            if (room[i] == room[j] && i != j)
            {
                room[i] = -1;
            }
            else if(i == j){
                break;
            }
        }
    }
    for (int i = 0; i < 10; i++)
    {
        if (room[i] != -1)
            cnt++;
    }
    printf("%d",cnt);
    
}