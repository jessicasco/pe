#include <iostream>
using namespace std;

int main() {
    int a[1000], b[1000];
    int i, j, n, m, curlength, remain;
    int maxlength = 0;
    m = 2;
    for(n = 2; n < 1000; n++){
        curlength = 0;
        remain = 10;
        for(i = 0; ; i++){
            a[i] = remain/n;
            b[i] = remain%n;        
            for(j = 0; j < i; j++){
                if(a[j] == a[i] && b[j] == b[i]){
                    curlength = i-j;
                    break;
                }
            }
            if(curlength != 0)
                break;
            remain = 10*b[i];
            if(remain == 0){
                break;
            }
        }
        if(curlength > maxlength){
            maxlength = curlength;
            m = n;
        }
    }   
    cout << m << endl;
    return 0;
}
