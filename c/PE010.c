#include <stdio.h>
#include <math.h>

void theSieveOfEratosthenes(int sieve[], int sievebound, int limit);

int main()
{
    long long sum = 2;
    int limit = 2000000;
    int sievebound = (limit-1)/2;
    int sieve[sievebound+1];
    theSieveOfEratosthenes(sieve, sievebound, limit);
    for(int i = 1; i <= sievebound; i++)
        if(!sieve[i])
            sum += 2*i + 1;
    printf("%lld\n", sum);
    return 0;
}

void theSieveOfEratosthenes(int sieve[], int sievebound, int limit)
{
    for(int i = 0; i <= sievebound; i++)
        sieve[i] = 0;
    int crosslimit =((int)sqrt(limit)-1)/2;
    for(int i = 1; i <= crosslimit; i++)
        if(!sieve[i])
            for(int j=2*i*(i+1); j <= sievebound; j += 2*i+1)
                sieve[j] = 1;
}
