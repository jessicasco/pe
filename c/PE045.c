#include <stdio.h>
#include <math.h>

int isPentagonal(long long m)
{
    long long k = 1 + 24*m;
    int t = (int)(sqrt(k)+0.1);
    long long l = (1+t)/6;
    if((l*(3*l-1))/2 == m)
        return 1;
    return 0;
}
int isHexagonal(long long m){
    long long k = 1 + 8*m;
    int t = (int)(sqrt(k)+0.1);
    int l = (1+t)/4;
    if((l*(2*l-1)) == m)
        return 1;
    return 0;
}
int main()
{
    long long i;
    long long m;
    for(i = 286; ; i++){
        m = (i*(i+1))/2;
        if(isPentagonal(m) && isHexagonal(m))
            break;
    }
    printf("%lld\n", m);
    return 0;
}
