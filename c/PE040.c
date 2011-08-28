#include <stdio.h>
#define MAX 1000000
int a[MAX+100],b[100];
int main() {
    int i, j, k, m;
    k = 1;
    for(i = 1; ; i++){
        j = i;
        m = 0;
        while(j){
            b[m] = j%10;
            j /= 10;
            m++;
        }
        for(m--; m >= 0; m--){
            a[k] = b[m];
            k++;
        }
        if(k > MAX)
            break;
    }
    int res = a[1]*a[10]*a[100] * a[1000] * a[10000] * a[100000] * a[1000000];
    printf("%d\n", res);
    return 0;
}
