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
    int i, j, t;
    for(i = 9; ; i += 2){
        if(isPrime(i))
            continue;
        for(j = 1; 2*j*j < i; j++){
            t = i-2*j*j;
            if(isPrime(t))
                break;
        }
        if(2*j*j >= i)
            break;
    }
    cout << i << endl;
    return 0;
}
