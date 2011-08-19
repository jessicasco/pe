#include <stdio.h>

int main(int argc, const char *argv[])
{
    long long n = 600851475143ll;
    int m = 1;
    int i;
    for (i = 3; i*i <= n; i+=2) {
        while (n%i == 0) {
            n /= i;
            m = i;
        }
    }
    if (n != 1) {
        printf("%lld\n", n);
    }
    else {
        printf("%d\n", m);
    }
    return 0;
}
