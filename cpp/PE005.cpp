#include <iostream>
#include <cmath>
using namespace std;

int main(int argc, const char *argv[])
{
    int primeList[] = {2, 3, 5, 7, 11, 13, 17, 19};
    int result = 1;
    for (int i = 0; i < 8; i++) {
        int maxPower = (int)floor(log(20)/log(primeList[i]));
        result *= (int)pow(primeList[i], maxPower);
    }
    cout << result << endl;
    return 0;
}
