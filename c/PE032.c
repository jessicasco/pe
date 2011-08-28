#include <stdio.h>
#include <math.h>

int main() {
    int i, j, k, m, n, sum = 0;
    int a[10];
    for(i = 1000; i <= 9999; i++){
        k = sqrt(i);
        for(j = 2; j <= k+1; j++) {
            if(i%j == 0) {
                for(m = 0; m < 10; m++)
                    a[m] = 0;
                n = 0;
                m = i;
                while(m) {
                    a[m%10] = 1;
                    m /= 10;
                    n++;
                }
                m = j;
                while(m) {
                    a[m%10] = 1;
                    m /= 10;
                    n++;
                }
                m = i/j;
                while(m){
                    a[m%10] = 1;
                    m /= 10;
                    n++;
                }
                for(m = 1; m < 10; m++)
                    if(a[m] == 0)
                        break;
                if(m == 10 && n == 9){
                    sum += i;
                    break;
                }
            }
        }
    }
    printf("%d\n", sum);
    return 0;
}
