#include <stdio.h>
#include <math.h>

int isPrime(int n)
{
    if(n <= 0)
        return 0;
    if(n == 1)
        return 0;
    else if(n < 4)
        return 1;
    else if(n%2 == 0)
        return 0;
    else if(n < 9)
        return 1;
    else if(n%3 == 0)
        return 0;
    else{
        int r = (int)sqrt((double)n);
        int f = 5;
        while(f <= r){
            if(n%f == 0)
                return 0;
            else if(n%(f+2) == 0)
                return 0;
            f += 6;
        }
    }
    return 1;
}
int main()
{
    int i, j, t;
    for(i = 9; ; i += 2){
        if(isPrime(i))
            continue;
        for(j = 1; 2*j*j < i; j++){
            t = i-2*j*j;
            if(isPrime(t))
                break;
        }
        if(2*j*j >= i)
            break;
    }
    printf("%d\n", i);
    return 0;
}
