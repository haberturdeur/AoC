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
            cout << data.back() << endl;
        }
        myfile.close();

        for (auto& i : data) {
            for (auto& j : data) {
                for (auto& k : data) {
                    if ((i + j + k) == 2020) {
                        a = i;
                        b = j;
                        d = k;
                        c = 1;
                        break;
                    }
                }
                if (c)
                    break;
            }
            if (c)
                break;
        }
        cout << "a: " << a << endl
             << "b: " << b << endl
             << "d: " << d << endl;
        cout << "result" << a * b * d;

    }

    else
        cout << "Unable to open file";

    return 0;
}