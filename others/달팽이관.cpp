#include<stdio.h>
int main(){
    int n,cnt = 0,x = 0,y = 0,sw = 1;
    scanf("%d",&n);
    int ori = n;
    int room[n][n];
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            room[i][j] = 0;
        }
    }
    for (y = 0; y < n; y++){
        room[x][y] = ++cnt;
    }
    n--;
    y--;
    while (n != 0)
    {
        if (sw == 1)
        {   
            x++;
            for(int i = 0; i < n; i++)
                room[x++][y] = ++cnt;
            x--;
            y--;
            for(int i = 0; i < n; i++)
                room[x][y--] = ++cnt;
            y++;
            sw = -1;
        }
        else{
            x--;
            for (int i = 0; i < n; i++){
                room[x--][y] = ++cnt;
            }
            x++;
            y++;
            for (int i = 0; i < n ; i++)
                room[x][y++] = ++cnt;
            y--;
            sw = 1;
        }
        n--;

    }
    for (int i = 0; i < ori; i++)
    {
        for (int j = 0; j < ori; j++)
        {
            printf("%3d ", room[i][j]);
        }
        printf("\n");
    }
}
