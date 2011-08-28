#include <stdio.h>

int a[100];
int isPalindromic(int n, int base)
{
    int i = 0, j, k;
    while(n){
        a[i] = n%base;
        i++;
        n /= base;
    }
    for(j = 0, k = i-1; j < k; j++, k--){
        if(a[j] != a[k])
            return 0;
    }
    return 1;
}

int main()
{
    int i, sum = 0;
    for(i = 1; i < 1000000; i++){
        if(isPalindromic(i, 2) && isPalindromic(i, 10)){
            sum += i;
        }
    }
    printf("%d\n", sum);
    return 0;
}
