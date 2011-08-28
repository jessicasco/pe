#include <iostream>
using namespace std;
int a[1001][3001];
int b[10];
int main() {
    int i, j, k, carry, m;
    for(i = 0; i < 10; i++)
        b[i] = 0;
    for(i = 1; i <= 1000; i++){
        a[i][0] = 1;
        for(j = 1; j <= 3000; j++)
            a[i][j] = 0;
    }
    for(i = 1; i <= 1000; i++){
        for(j = 1; j <= i; j++){
            carry = 0;
            for(k = 0; k <= 3000; k++){
                m = a[i][k]*i + carry;
                a[i][k] = m%10;
                carry = m/10;
            }
        }
    }
    carry = 0;
    for(i = 0; i < 10; i++){
        m = carry;
        for(j = 1; j <= 1000; j++)
            m += a[j][i];
        b[i] = m%10;
        carry = m/10;
    }
    for(i = 9; i >= 0; i--)
        cout << b[i];
    cout << endl;
    return 0;
}
