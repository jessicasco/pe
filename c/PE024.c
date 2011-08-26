#include <stdio.h>
#include <stdlib.h>

int cmp (const void *a, const void *b) {
    return *(int *)a - *(int *)b;
}
void lexicographical_sort(int a[], int n) {
    int i, j, t;
    for(i = n-1; i > 0; i--){
        if(a[i] > a[i-1]){
            for(j = n-1; ; j--)
                if(a[j] > a[i-1]){
                    t = a[j];
                    break;
                }
            a[j] = a[i-1];
            a[i-1] = t;
            qsort(a+i, n-i, sizeof(int), cmp);
            break;
        }
    }
}

int main() {
    int i;
    int a[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    for(i = 1; i < 1000000; i++)
        lexicographical_sort(a, 10);
    for(i = 0; i < 10; i++)
        printf("%d", a[i]);
    printf("\n");
    return 0;
}
