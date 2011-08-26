#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main()
{
    freopen("PE022.txt", "r", stdin);
    char c;
    int i = 0, j = 0;
    char s[5200][20];
    int flag = 0;
    while(scanf("%c", &c) == 1){
        if(c == ',')
            continue;
        if(c == '\"'){
            if(flag == 0){
                flag = 1;
                j = 0;
            }
            else{
                flag = 0;
                s[i][j++] = '\0';
                i ++;
            }
        }               
        else
            s[i][j++] = c;
    }
    qsort((void *)s, i, sizeof(char) * 20, 
            (int (*) (const void *, const void *))strcmp);
    long long result = 0;
    for(int k = 0; k < i; k++) {
        int value = 0;
        for(int j = 0; s[k][j] != '\0'; j++)
            value += s[k][j] - 'A' + 1;
        result += (k + 1) * value;
    }
    printf("%lld\n", result);
    return 0;
}
