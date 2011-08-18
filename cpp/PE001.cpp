#include <iostream>
using namespace std;

int f(int, int);

int main (int argc, char const* argv[])
{
    cout << f(3, 1000) + f(5, 1000) - f(3 * 5, 1000) << endl;
    return 0;
}

int f(int a, int b) {
    int n = (b - 1) / a;
    return a * (n * (n + 1) / 2);
}
