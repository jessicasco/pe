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
    int limit = 10001;
    int count = 1;
    int candidate = 1;
    do{
        candidate += 2;
        if(isPrime(candidate))
            count++;
    }while(count < limit);
    cout << candidate << endl;
    return 0;
}
