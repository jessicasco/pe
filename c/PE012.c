#include <stdio.h>

int numOfdivisors(int n);

int main(int argc, const char *argv[])
{
    int i = 1;
    int n = i*(i+1)/2;
    while (numOfdivisors(n) <= 500) {
        i += 1;
        n = i*(i+1)/2;
    }
    printf("%d\n", n);
    return 0;
}

int numOfdivisors(int n) {
    int res = 1;
    int count = 1;
    while (n%2 == 0) {
        n /= 2;
        count += 1;
    }
    res *= count;
    int i = 3;
    while (i*i <= n && n > 1) {
        count = 1;
        while (n%i == 0) {
            n /= i;
            count += 1;
        }
        res *= count;
        i += 2;
    }
    if (n > 1) 
        res *= 2;
    return res;
}
