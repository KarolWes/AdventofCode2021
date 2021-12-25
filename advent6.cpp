#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

int main(){

    fstream f;
    int n;
    f.open("tmp.txt", ios::in);
    vector <unsigned long long int> l;
    for(int i = 0; i < 9; i++)
    {
        l.push_back(0);
    }
    while(!f.eof()){
        f >> n;
        l[n]++;
    }
    for(int i= 0; i < 256; i++){
        cout << i << endl;
        unsigned long long int first = l[0];
        for(int j = 1; j < 9; j++ )
        {
            l[j-1] = l[j];
        }
        l[8]+=first;
        l[6]+=first;
    }
    unsigned long long int res;
    for(int i = 0; i < 9; i++){
        res+=l[i];
    }
    cout << res;
    return 0;
}
