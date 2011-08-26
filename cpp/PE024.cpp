#include <iostream>
#include <algorithm>
using namespace std;

void lexicographical_sort(int a[], int n) {
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

int main() {
    int i;
    int a[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    for(i = 1; i < 1000000; i++)
        lexicographical_sort(a, 10);
    for(i = 0; i < 10; i++)
        cout << a[i];
    cout << endl;
    return 0;
}
