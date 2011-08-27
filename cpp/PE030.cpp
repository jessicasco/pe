#include <iostream>
using namespace std;

bool isProper(int n) {
    int k = 0, m = n, l;
    while(m){
        l = m%10;
        k += l*l*l*l*l;
        m /= 10;
    }
    return (k == n);
}

int main() {
    int i, sum = 0;
    for(i = 2; i < 1000000; i++){
        if(isProper(i))
            sum += i;
    }
    cout << sum << endl;
    return 0;
}
