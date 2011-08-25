#include <iostream>
using namespace std;

int main()
{
    int a[400];
    for(int i = 0; i < 400; i++)
        a[i] = -1;
    a[0] = 1;
    for(int i = 0; i < 1000; i++){
        int carry = 0;
        int j;
        for(j = 0; a[j] != -1; j++){
            int m = 2*a[j] + carry;
            a[j] = m%10;
            carry = m/10;
        }
        if(carry)
            a[j] = carry;
    }
    int sum = 0;
    for(int i = 0; a[i] != -1; i++)
        sum += a[i];
    cout << sum << endl;
    return 0;
}
