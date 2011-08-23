#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ifstream inf("PE008.txt");
    string s;
    string ss;
    while (getline(inf, s)) {
        ss += s;
    }
    int largestMul = 0;
    for (int i = 0; i <= (int)ss.size() - 5; i++) {
        int mul = 1;
        for(int j = 0; j < 5; j++)
            mul *= ss[i+j] - '0';
        if(mul > largestMul)
            largestMul = mul;
    }
    cout << largestMul << endl;
    return 0;
}
