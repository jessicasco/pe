#include <iostream>
#include <cmath>
using namespace std;

bool isPrime(long long n) {
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

int main() {
    long long a, b, n, max = 0, result;
    for(a = -999; a < 1000; a++){
        for(b = 2; b < 1000; b++){
            for(n = 0; ; n++){
                if(!isPrime(n*n+a*n+b)) 
                    break;
            }
            if(n > max){
                max = n;
                result = a*b;
            }
        }
    }
    cout << result << endl;
    return 0;
}
