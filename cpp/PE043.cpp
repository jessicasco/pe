#include <iostream>
#include <algorithm>
using namespace std;
void lexicographical_sort(int a[], int n)
{
    int i, j, t;
    for(i = n-1; i > 0; i--){
        if(a[i] > a[i-1]){
            for(j = n-1; ; j--)
                if(a[j] > a[i-1]){
                    t = a[j];
                    break;
                }
            a[j] = a[i-1];
            a[i-1] = t;
            sort(a+i, a+n);
            break;
        }
    }
}
int main()
{
    int i, j;
    long long m, sum = 0;
    int a[10] = {0, 9, 8, 7, 6, 5, 4, 3, 2, 1};
    int b[7];
    for(i = 1; i <= 3265920; i++){
        lexicographical_sort(a, 10);
        for(j = 0; j < 7; j++){
            b[j] = a[j+1]*100 + a[j+2]*10 + a[j+3];
        }
        if(b[0]%2==0&&b[1]%3==0&&b[2]%5==0&&b[3]%7==0&&b[4]%11==0&&b[5]%13==0&&b[6]%17==0) {
            m = 0;
            for(j = 0; j < 10; j++){
                m = 10*m + a[j];
            }
            sum += m;
        }
    }
    cout << sum << endl;
    return 0;
}
