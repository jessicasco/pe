#include <iostream>
#include <cmath>
using namespace std;
int a[10];
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

bool isCircularPrime(int n){
    if(!isPrime(n))
        return false;
    int i = 0;
    int j, k;
    while(n){
        a[i] = n%10; 
        i++;
        n /= 10;
    }
    for(j = i-2; j >= 0; j--){
        n = 0;
        for(k = j; k >= 0; k--)
            n = 10*n + a[k];
        for(k = i-1; k > j; k--)
            n = 10*n + a[k];
        if(!isPrime(n))
            return false;
    }
    return true;
}

int main() {
    int count = 0, i;
    for(i = 2; i < 1000000; i++){
        if(isCircularPrime(i)){
            count++;
        }
    }
    cout << count << endl;
    return 0;
}
