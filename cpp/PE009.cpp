#include <iostream>
#include <cmath>
using namespace std;

int gcd(int a, int b);
void getPythagoreanTriple(int s, int* res);

int main() {
    int s = 1000;
    int a[3];
    getPythagoreanTriple(s, a);
    cout << a[0] * a[1] * a[2] << endl;
    return 0;
}

int gcd(int a, int b) {
    int r;
    if(a < b){
        r = a;
        a = b;
        b = r;
    }
    while((r = a%b)){
        a = b;
        b = r;
    }
    return b;
}

void getPythagoreanTriple(int s, int* res) {
    int s2 = s/2;
    int mlimit = (int)ceil(sqrt((double)s2))-1;
    for(int m = 2; m <= mlimit; m++){
        if(s2%m != 0)
            continue;
        int sm = s2/m;
        int k;
        while(sm%2 == 0)
            sm /= 2;
        if(m%2 == 1)
            k = m+2;
        else
            k = m+1;
        while(k < 2*m && k <= sm){
            if(sm%k == 0 && gcd(k, m) == 1){
                int d = s2/(k*m);
                int n = k-m;
                res[0] = d*(m*m - n*n);
                res[1] = 2*d*m*n;
                res[2] = d*(m*m + n*n);
                return ;
            }
            k += 2;
        }
    }
}
