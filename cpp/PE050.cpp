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
int a[1000000];
int main()
{
    int i, j = 0, k, length = 0, max = 2, sum;
    for(i = 2; i <= 1000000; i++){
        if(isPrime(i)){
            a[j] = i;
            j++;
        }
    }
    for(i = 0; i < j; i++){
        sum = 0;
        for(k = i+length; k < j; k++){
            sum += a[k];
            if(sum > 1000000)
                break;
            if(isPrime(sum) && k-i+1 > length){
                length = k-i+1;
                max = sum;
            }
        }
    }
    cout << max << endl;
    return 0;
}
