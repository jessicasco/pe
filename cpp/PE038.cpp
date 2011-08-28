#include <iostream>
using namespace std;

int main()
{
    int i, j, k, m, n, x, t, a[10], max = 0;
    for(i = 2; i <= 9999; i++){
        for(j = 0; j < 10; j++){
            a[j] = 0;
        }
        k = 0;
        for(j = 1; j <= 6; j++){
            m = i*j;
            while(m){
                a[m%10] ++;
                m /= 10;
                k++;
            }
            if(k >= 9)
                break;
        }
        if(k == 9){
            for(n = 1; n < 10; n++){
                if(a[n] != 1)
                    break;
            }
            if(n == 10){
                m = 0;
                for(n = 1; n <= j; n++){
                    t = i*n;
                    x = 1;
                    while(x <= t){
                        x *= 10;
                    }
                    m = m*x + t;
                }
                if(m > max)
                    max = m;
            }
        }
    }
    cout << max << endl;
    return 0;
}
