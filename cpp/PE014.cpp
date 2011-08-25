#include <iostream>
using namespace std;

inline long long sequenceLength(long long n)
{
    long long length = 1;
    while(n != 1){
        length++;
        if(n%2 == 0)
            n /= 2;
        else
            n = 3*n+1;
    }
    return length;
}

int main()
{
    long long longestLength = 1;
    long long maxStart = 1;
    long long i, length;
    for(i = 2; i < 1000000; i++){
        length = sequenceLength(i);
        if(length > longestLength){
            longestLength = length;
            maxStart = i;
        }
    }
    cout << maxStart << endl;
    return 0;
}
