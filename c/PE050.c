#include <stdio.h>
#include <math.h>

int isPrime(int n) {
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
int a[1000000];
int main()
{
    int i, j = 0, k, length = 0, max = 2, sum;
    for(i = 2; i <= 1000000; i++){
        if(isPrime(i)){
            a[j] = i;
            j++;
        }
    }
    for(i = 0; i < j; i++){
        sum = 0;
        for(k = i; k < j; k++){
            sum += a[k];
            if(sum > 1000000)
                break;
            if(isPrime(sum) && k-i+1 > length){
                length = k-i+1;
                max = sum;
            }
        }
    }
    printf("%d\n", max);
    return 0;
}
