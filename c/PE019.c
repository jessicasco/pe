#include <stdio.h>

int main()
{
    int a[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    int i, j, count = 0, daySince = 0;
    for(i = 1901; i <= 2000; i++){
        for(j = 0; j < 12; j++){
            daySince += a[j];
            if((j == 1) && (i % 4) == 0)
                daySince ++;
            if((daySince % 7) == 5)
                count ++;
        }
    }
    printf("%d\n", count);
    return 0;
}
