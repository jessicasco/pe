#include <stdio.h>

int a[28123+1], b[28123+1];
int sumOfAllProperDivisors(int n) {
    int result = 0;
    int i;
    for(i = 1; i < n; i++)
        if(n%i == 0)
            result += i;
    return result;
}

int isAbundant(int n) {
    if(sumOfAllProperDivisors(n) > n)
        return 1;
    return 0;
}

int main() {
    int i, j = 0, k, result = 0;
    for(i = 1; i <= 28123; i++)
        a[i] = 0;
    for(i = 1; i <= 28123; i++){
        if(isAbundant(i))
            b[j++] = i;
    }
    for(i = 0; i < j; i++)
        for(k = i; k < j; k++){
            if(b[i] + b[k] <= 28123)
                a[b[i]+b[k]] = 1;
        }
    for(i = 1; i <= 28123; i++){
        if(a[i] == 0)
            result += i;
    }
    printf("%d\n", result);
    return 0;
}
