#include <stdio.h>

int reverse(int n);
int isPalindrome(int n);

int main(int argc, const char *argv[])
{
    int max = 0;
    for(int a=999; a >= 100; a-=1) {
        int step, b;
        if (a%11 == 0) {
            step = 1;
            b = a;
        }
        else {
            step = 11;
            b = a/11*11;
        }
        if (max != 0 && a*b <= max) {
            break;
        }
        while (b >= 100) {
            int s = a * b;
            if (max != 0 && s <= max) {
                break;
            }
            if (isPalindrome(s)) {
                max = s;
            }
            b -= step;
        }
    }
    printf("%d\n", max);
    return 0;
}

int reverse(int n)
{
    int reverse = 0;
    while(n > 0){
        reverse = 10*reverse + n%10;
        n /= 10;
    }
    return reverse;
}

int isPalindrome(int n)
{
    return n == reverse(n);
}

