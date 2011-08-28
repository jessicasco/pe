#include <stdio.h>
#include <math.h>

int isFour(int n)
{
    int i, j = 0;
    for(i = 2; i <= n; i++){
        if(n%i == 0){
            j++;
            n /= i;
        }
        while(n%i == 0)
            n /= i;
    }
    return (j == 4);
}
int main()
{
    int i, j;
    for(i = 2; ; i++){
        for(j = i; j < i+4; j++){
            if(!isFour(j))
                break;
        }
        if(j == i+4)
            break;
    }
    printf("%d\n", i);
    return 0;
}
