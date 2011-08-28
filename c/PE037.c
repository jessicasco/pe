#include <stdio.h>
#include <math.h>

int isPrime(int n)
{
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
int isTruncatable(int n){
    int m = n, i = 1;
    m /= 10;
    while(m){
        if(!isPrime(m))
            return 0;
        i *= 10;
        m /= 10;
    }
    m = n;
    while(i != 1){
        m = m%i;
        if(!isPrime(m))
            return 0;
        i /= 10;
    }
    return 1;
}
int main()
{
    int i, count = 0, sum = 0;
    for(i = 11; ; i += 2){
        if(isPrime(i) && isTruncatable(i)){
            count++;
            sum += i;
        }
        if(count == 11)
            break;
    }
    printf("%d\n", sum);
    return 0;
}
