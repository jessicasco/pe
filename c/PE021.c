#include <stdio.h>

int d(int n)
{
    int result = 0;
    int i;
    for(i = 1; i < n; i++)
        if(n%i == 0)
            result += i;
    return result;
}

int main()
{
    int i, sum = 0, b;
    for(i = 1; i < 10000; i++){
        if((b = d(i)) > i && d(b) == i)
            sum += i + b;
    }
    printf("%d\n", sum);
    return 0;
}
            
