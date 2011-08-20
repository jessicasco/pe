#include <stdio.h>

long long sumOfSquares(int n)
{
    return n*(n+1)*(2*n+1)/6;
}
long long squareOfSums(int n)
{
    long long a = n*(n+1)/2;
    return a * a;
}
int main()
{
    printf("%lld\n", squareOfSums(100) - sumOfSquares(100));
    return 0;
}
