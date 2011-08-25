#include <stdio.h>

int main()
{
    int a[200], i, j, m, count, carry;
    for(j = 0; j < 200; j++)
        a[j] = 0;
    a[0] = 1;
    count = 0;
    for(i = 2; i <= 100; i++){
        carry = 0;
        for(j = 0; j < 200; j++){
            m = a[j] * i + carry;
            a[j] = m%10;
            carry = m/10;
        }
    }
    for(j = 0; j < 200; j++)
        count += a[j];
    printf("%d\n", count);
    return 0;
}
