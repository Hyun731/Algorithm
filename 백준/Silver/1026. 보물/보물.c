#include <stdio.h>

void selection_sort1(int arr[], int n) {
    int i, j, min_idx;
    for (i = 0; i < n-1; i++) {
        min_idx = i;
        for (j = i+1; j < n; j++)
            if (arr[j] < arr[min_idx])
                min_idx = j;

        int temp = arr[min_idx];
        arr[min_idx] = arr[i];
        arr[i] = temp;
    }
}
void selection_sort2(int arr[], int n) {
    int i, j, min_idx;
    for (i = 0; i < n-1; i++) {
        min_idx = i;
        for (j = i+1; j < n; j++)
            if (arr[j] > arr[min_idx])
                min_idx = j;

        int temp = arr[min_idx];
        arr[min_idx] = arr[i];
        arr[i] = temp;
    }
}

int main() {
    int n;
    scanf("%d",&n);
    int a[n];
    int b[n];
    int sum = 0;
    for(int i = 0; i < n; i++){
        scanf("%d",&a[i]);
    }
    for(int i = 0; i < n; i++){
        scanf("%d",&b[i]);
    }
    selection_sort1(a,n);
    selection_sort2(b,n);
    for(int i = 0; i < n; i++){
        sum += a[i] * b[i];
    }
    printf("%d",sum);
    
}