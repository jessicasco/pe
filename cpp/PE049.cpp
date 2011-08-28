#include <iostream>
#include <cmath>
using namespace std;
bool isPrime(int n)
{
    if(n <= 0)
        return false;
    if(n == 1)
        return false;
    else if(n < 4)
        return true;
    else if(n%2 == 0)
        return false;
    else if(n < 9)
        return true;
    else if(n%3 == 0)
        return false;
    else{
        int r = (int)sqrt((double)n);
        int f = 5;
        while(f <= r){
            if(n%f == 0)
                return false;
            else if(n%(f+2) == 0)
                return false;
            f += 6;
        }
    }
    return true;
}
int main()
{
    int i, j, k, t;
    int a[10], b[10], c[10];
    for(i = 1000; i <= 9997; i++){
        for(j = 1; i+2*j <= 9999; j++){
            if(isPrime(i) && isPrime(i+j) && isPrime(i+2*j)){
                for(k = 0; k < 10; k++){
                    a[k] = 0;
                    b[k] = 0;
                    c[k] = 0;
                }
                t = i;
                while(t){
                    a[t%10] ++;
                    t /= 10;
                }
                t = i+j;
                while(t){
                    b[t%10] ++;
                    t /= 10;
                }
                t = i+2*j;
                while(t){
                    c[t%10] ++;
                    t /= 10;
                }
                for(k = 0; k < 10; k++){
                    if(a[k] == b[k] && b[k] == c[k])
                        continue;
                    break;
                }
                if(k == 10 && !(i == 1487 && j == 3330)){
                    cout << i << i+j << i+2*j << endl;
                    return 0;
                }
            }           
        }
    }
}
