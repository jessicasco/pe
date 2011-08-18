#include <stdio.h>

int f(int, int);
int main (int argc, char const* argv[])
{
    printf("%d\n", f(3, 1000) + f(5, 1000) - f(3 * 5, 1000));
    return 0;
}

int f(a, b) {
    int n = (b - 1) / a;
    return a * (n * (n + 1) / 2);
}
