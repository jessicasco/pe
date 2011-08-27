#include <iostream>
using namespace std;

int main() {
    int i, j, a = 1, sum = 1, step;
    for(i = 1; i <= (1001-1)/2; i++){
        step = 2*i;
        for(j = 1; j <= 4; j++){
            a += step;
            sum += a;
        }
    }
    cout << sum << endl;
    return 0;
}
