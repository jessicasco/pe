#include <stdio.h>

int main()
{
    freopen("PE008.txt", "r", stdin);
    char s[1000], c;
    int i = 0;
    while (scanf("%c", &c) == 1) {
        if ( c >= '0' && c <= '9') {
            s[i++] = c - '0';
        }
    }
    int largestMul = 0;
    for (int i = 0; i <= 1000 - 5; i++) {
        int mul = 1;
        for(int j = 0; j < 5; j++)
            mul *= s[i+j];
        if(mul > largestMul)
            largestMul = mul;
    }
    printf("%d\n", largestMul);
    return 0;
}
