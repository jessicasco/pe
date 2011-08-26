#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main()
{
    ifstream infile("PE022.txt");
    char c;
    string s;
    vector<string> v;
    bool flag = false;
    while(infile>>c){
        if(c == ',')
            continue;
        if(c == '\"'){
            if(flag == false){
                flag = true;
                s.erase();
            }
            else{
                flag = false;
                v.push_back(s);
            }
        }               
        else{
            s.insert(s.end(), c);
        }
    }
    sort(v.begin(), v.end());
    vector<string>::iterator pos;
    int i = 1;
    long long result = 0;
    for(pos = v.begin(); pos != v.end(); pos++){
        s = *pos;       
        int value = 0;
        for(int j = 0; j < (int)s.length(); j++)
            value += s[j] - 'A' + 1;
        result += i * value;
        i++;
    }
    cout << result << endl;
    infile.close();
    return 0;
}
