#include <fstream>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main()
{
    string line;
    vector<unsigned> data;
    int a, b, c, d;
    ifstream myfile("data.txt");
    if (myfile.is_open()) {
        while (getline(myfile, line)) {
            data.push_back(stoi(line));
            // cout << data.back() << endl;
        }
        myfile.close();
        for (int i = 3; i < data.size(); i++)
        {
            a += data[i]+data[i-1] + data[i-2]>data[i-1] + data[i-2] +data[i-3];
        }
        cout << a << endl;
    }

    else
        cout << "Unable to open file";

    return 0;
}