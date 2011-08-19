#include <stdio.h>

int main(int argc, const char *argv[])
{
    int a = 2;
    int b = 8;
    int sum = a + b;
    int c = 4*b + a;
    while (c <= 4000000) {
        sum += c;
        a = b;
        b = c;
        c = 4*b + a;
    }
    printf("%d\n", sum);
    return 0;
}
