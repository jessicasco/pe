#include <stdio.h>
#include <math.h>
int a[10];
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

int isCircularPrime(int n){
    if(!isPrime(n))
        return 0;
    int i = 0;
    int j, k;
    while(n){
        a[i] = n%10; 
        i++;
        n /= 10;
    }
    for(j = i-2; j >= 0; j--){
        n = 0;
        for(k = j; k >= 0; k--)
            n = 10*n + a[k];
        for(k = i-1; k > j; k--)
            n = 10*n + a[k];
        if(!isPrime(n))
            return 0;
    }
    return 1;
}

int main() {
    int count = 0, i;
    for(i = 2; i < 1000000; i++){
        if(isCircularPrime(i)){
            count++;
        }
    }
    printf("%d\n", count);
    return 0;
}
