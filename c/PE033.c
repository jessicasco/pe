#include <stdio.h>

int main() {
    int a, b, c, d, s = 1, result = 1;
    for(a = 11; a < 100; a++){
        for(b = 10+a/10; b < a; b += 10){
            c = b/10;
            d = a%10;
            if(a*c == b*d){
                s *= c;
                result *= d;
            }
        }
    }
    for(int i = 2; i <= s; i++){
        if(s%i == 0 && result%i == 0){
            result /= i;
            s /= i;
        }
    }
    printf("%d\n", result);
    return 0;
}
