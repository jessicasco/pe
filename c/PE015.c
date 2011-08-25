#include <stdio.h>

long long Combination(int n, int m)
{
    if(n-m < m)
        m = n-m;
    int i;
    double result = 1;
    for(i = 0; i < m; i++)
        result *= (n-i)*1.0/(i+1);
    return (long long)result;
}

int main()
{
    printf("%lld\n", Combination(20+20, 20));
    return 0;
}
