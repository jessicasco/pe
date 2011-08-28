#include <iostream>
#include <cmath>
using namespace std;
bool isPrime(int n)
{
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
    int max = 0, a[10], k, i, j, m;
    for(i = 2; i <= 9876543; i++){
        if(isPrime(i)){
            for(j = 0; j < 10; j++)
                a[j] = 0;
            k = 0;
            m = i;
            while(m){
                k++;
                a[m%10] ++;
                m /= 10;
            }
            for(j = 1; j <= k; j++){
                if(a[j] == 0)
                    break;
            }
            if(j == k+1 && i >= max)
                max = i;
        }
    }
    cout << max << endl;
    return 0;
}
