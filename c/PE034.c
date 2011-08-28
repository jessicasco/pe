#include <stdio.h>

int a[10];
int main() {
    int isProper(int);
    int i, sum = 0;
    a[0] = 1;
    for(i = 1; i < 10; i++){
        a[i] = i*a[i-1];
    }
    for(i = 3; i < 10000000; i++){
        if(isProper(i))
            sum += i;
    }
    printf("%d\n", sum);
    return 0;
}
int isProper(int n) {
    int m = n, res = 0;
    while(m){
        res += a[m%10];
        m /= 10;
    }
    return (res == n);
}
