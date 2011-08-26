#include <iostream>
using namespace std;

int a[1000], b[1000], c[1000];
void clear_array(int c[], int n) {
    int i;
    for(i = 0; i < n; i++)
        c[i] = 0;
}

void copy(int a[], int b[], int n) {
    int i;
    for(i = 0; i < n; i++)
        a[i] = b[i];
}

void add(int c[], int a[], int b[], int n) {
    int i, t;
    for(i = 0; i < n; i++){
        t = a[i] + b[i] + c[i];
        c[i] = t%10;
        c[i+1] = t/10;
    }
}

int main() {
    int i, k = 2;
    for(i = 0; i < 1000; i++){
        a[i] = 0;
        b[i] = 0;
        c[i] = 0;
    }
    a[0] = 1;
    b[0] = 1;
    while(!a[999]){
        add(c, a, b, 1000);
        copy(b, a, 1000);
        copy(a, c, 1000);
        clear_array(c, 1000);
        k++;
    }
    cout << k << endl;
    return 0;
}
