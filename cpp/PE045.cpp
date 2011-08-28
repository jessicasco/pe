#include <iostream>
#include <cmath>
using namespace std;

bool isPentagonal(long long m)
{
    long long k = 1 + 24*m;
    int t = int(sqrt(k)+0.1);
    long long l = (1+t)/6;
    if((l*(3*l-1))/2 == m)
        return true;
    return false;
}
bool isHexagonal(long long m){
    long long k = 1 + 8*m;
    int t = int(sqrt(k)+0.1);
    int l = (1+t)/4;
    if((l*(2*l-1)) == m)
        return true;
    return false;
}
int main()
{
    long long i;
    long long m;
    for(i = 286; ; i++){
        m = (i*(i+1))/2;
        if(isPentagonal(m) && isHexagonal(m))
            break;
    }
    cout << m << endl;
    return 0;
}
