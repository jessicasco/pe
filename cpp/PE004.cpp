#include <iostream>
using namespace std;

int main(int argc, const char *argv[])
{
    int max = 0;
    for(int a=999; a >= 100; a-=1) {
        int step, b;
        if (a%11 == 0) {
            step = 1;
            b = a;
        }
        else {
            step = 11;
            b = a/11*11;
        }
        if (max != 0 && a*b <= max) {
            break;
        }
        while (b >= 100) {
            int s = a * b;
            if (max != 0 && s <= max) {
                break;
            }
            int c[100], i = 0, j;
            int s1 = s;
            while (s1) {
                c[i++] = s1 % 10;
                s1 /= 10;
            }
            for(j=0, i-=1; i > j; i-=1, j+=1) {
                if (c[i] != c[j]) {
                    break;
                }
            }
            if(i <= j) {
                max = s;
            }
            b -= step;
        }
    }
    cout << max << endl;
    return 0;
}
