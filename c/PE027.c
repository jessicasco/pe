#include <stdio.h>
#include <math.h>

int isPrime(long long n) {
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

int main() {
    long long a, b, n, max = 0, result;
    for(a = -999; a < 1000; a++){
        for(b = 2; b < 1000; b++){
            for(n = 0; ; n++){
                if(!isPrime(n*n+a*n+b)) 
                    break;
            }
            if(n > max){
                max = n;
                result = a*b;
            }
        }
    }
    printf("%lld\n", result);
    return 0;
}
