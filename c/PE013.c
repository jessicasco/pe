#include <string.h>
#include <stdio.h>

#define N 52

void reverse(char *s) {
    int k = strlen(s);
    for(int i = 0, j = k-1; i < j; i++, j--) {
        char temp = s[i];
        s[i] = s[j];
        s[j] = temp;
    }
    s[k] = '0';
}

void sum(char *s, char *a, char *b) {
    int sum, carry = 0;
    for(int i = 0; i < N; i++){
        sum = a[i]-'0' + b[i]-'0' + carry;
        s[i] = '0' + sum%10;
        carry = sum/10;
    }
}

void copy(char *s, char *t) {
    int i;
    for(i = 0; i < N; i++)
        s[i] = t[i];
}

int main() {
    FILE *fp = fopen("PE013.txt", "r");
    char s[N], a[N], b[N];
    int i;
    for(i = 0; i < N; i++){
        s[i] = '0';
        a[i] = '0';
        b[i] = '0';
    }
    for(i = 0; i < 100; i++){
        fgets(a, 50+1, fp);
        fgetc(fp);
        reverse(a);
        sum(b, s, a);
        copy(s, b);
    }
    for(i = N-1; s[i] == '0'; i--)
        ;
    for(int j = 0; j < 10; j++){
        printf("%c",s[i]);
        i--;
    }
    printf("\n");
    return 0;
}
