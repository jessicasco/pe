#include <stdio.h>
#include <math.h>

int isPrime(int n);

int main() {
    int limit = 10001;
    int count = 1;
    int candidate = 1;
    do{
        candidate += 2;
        if(isPrime(candidate))
            count++;
    }while(count < limit);
    printf("%d\n", candidate);
    return 0;
}

int isPrime(int n) {
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
