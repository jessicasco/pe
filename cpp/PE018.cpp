#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

int main()
{
    int a[15][15];
    ifstream in("PE018.txt");
    for(int i=0; i < 15; i++) {
        for(int j=0; j <= i; j++) {
            in >> a[i][j];
        }
    }
    int k = (int)pow(2, 14);
    int i, j, l, m, max, curmax;
    max = 0;
    for(i = 0; i < k; i++){
          l = i;
          curmax = a[0][0];
          m = 0;
          for(j = 0; j < 14; j++){
            m += l%2;
            l/=2;
            curmax += a[j+1][m];
          }
          if(curmax > max)
            max = curmax;
    }
    cout << max << endl;
    return 0;
}
