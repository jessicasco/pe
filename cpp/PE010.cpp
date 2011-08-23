#include <iostream>
#include <vector>
#include <cmath>
using namespace std; 

vector<int> getPrimeList(int limit);

int main()
{
    long long sum = 0;
    vector<int> Sieve = getPrimeList(2000000);
    for(vector<int>::const_iterator p = Sieve.begin(); p != Sieve.end(); p++)
        sum += *p;
    cout << sum << endl;
    return 0;
}

vector<int> getPrimeList(int limit) {
    int sievebound = (limit-1) / 2;
    vector<bool> sieve;
    for(int i = 0; i <= sievebound; i++)
        sieve.push_back(false);
    int crosslimit =((int)sqrt(limit)-1)/2;
    for(int i = 1; i <= crosslimit; i++)
        if(!sieve[i])
            for(int j=2*i*(i+1); j <= sievebound; j += 2*i+1)
                sieve[j] = true;
    vector<int> Sieve;
    Sieve.push_back(2);
    for (int i = 1; i <= sievebound; i++) {
        if(!sieve[i])
            Sieve.push_back(2*i+1);
    }
    return Sieve;
}
