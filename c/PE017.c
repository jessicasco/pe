#include <stdio.h>

int main()
{
    int a[20] = {0,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8};//0-19
    int b[10] = {6,6,5,5,5,7,6,6};//2-9
    
    int sum = 0;
    for(int i = 1; i < 1000; i++){
        int j = (i%100)/10;
        if(j == 0)
            sum += a[i%10];
        else if(j == 1){
            sum += a[i%100];
        }
        else if(j >= 2){
            sum += b[j-2] + a[i%10];
        }
        if(i/100)
            sum += a[i/100] + 7 + 3;
        if(i/100 && i%100 == 0)
            sum -= 3;
    }
    sum += 11;
    printf("%d\n", sum);
    return 0;
}
