#include <stdio.h>
#include <math.h>

int main() {
    double answer[10000];
    int i = 0;
    for (double a = 2; a<=100;a++)
        for (double b = 2;b<=100;b++) {
            double temp = pow(a,b);
            int j;
            for(j = 0; j < i; j++) {
                if (answer[j] == temp)
                    break;
            }
            if (j == i)
                answer[i++] = temp;
        }
    printf("%d\n", i);
    return 0;
}
