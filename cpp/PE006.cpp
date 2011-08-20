#include <iostream>
using namespace std;

long long sumOfSquares(int n)
{
    return n*(n+1)*(2*n+1)/6;
}
long long squareOfSums(int n)
{
    long long a = n*(n+1)/2;
    return a * a;
}
int main()
{
    cout << squareOfSums(100) - sumOfSquares(100) << endl;
    return 0;
}
