#include <stdio.h>

int main()
{
    int a, b, c, p, max = 0, size, maxp = 0;
    for(p = 12; p <= 1000; p++){
        size = 0;
        for(a = 3; a <= (p-3)/3; a++){
            for(b = a+1; b <= (p-4)/2; b++){
                c = p-a-b;
                if(c*c == a*a + b*b)
                    size++;
            }
        }
        if(size > max){
            max = size;
            maxp = p;
        }
    }
    printf("%d\n", maxp);
    return 0;
}
