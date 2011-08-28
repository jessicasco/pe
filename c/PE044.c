#include <stdio.h>
#include <math.h>

int isPentagonal(long long n)
{
    int t = (1+(int)(sqrt(1+24*n)))/6;
    return ((t*(3*t-1))/2 == n);
}
int main()
{
    long long i, j, m, n, min = 0;
    for(i = 1; ; i++) {
        m = (i*(3*i-1))/2 - ((i-1)*(3*(i-1)-1))/2;
        if(m > min && min != 0)
            break; 
        for(j = i-1; j > 0 ; j--) {
            m = (i*(3*i-1))/2 - (j*(3*j-1))/2;
            if(m > min && min != 0)
                break;
            n = (i*(3*i-1))/2 + (j*(3*j-1))/2;
            if(isPentagonal(m) && isPentagonal(n)){
                min = m;
            }
        }
    }
    printf("%lld\n", min);
    return 0;
}
