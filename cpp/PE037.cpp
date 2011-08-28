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
bool isTruncatable(int n){
    int m = n, i = 1;
    m /= 10;
    while(m){
        if(!isPrime(m))
            return false;
        i *= 10;
        m /= 10;
    }
    m = n;
    while(i != 1){
        m = m%i;
        if(!isPrime(m))
            return false;
        i /= 10;
    }
    return true;
}
int main()
{
    int i, count = 0, sum = 0;
    for(i = 11; ; i += 2){
        if(isPrime(i) && isTruncatable(i)){
            count++;
            sum += i;
        }
        if(count == 11)
            break;
    }
    cout << sum << endl;
    return 0;
}
