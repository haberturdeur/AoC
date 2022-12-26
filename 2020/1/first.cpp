#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
    string line;
    vector<int> data;
    ifstream myfile("data.txt");
    if (myfile.is_open()) {
        while (getline(myfile, line)) {
            int a = stoi(line);
        }
        myfile.close();
        cout << data.length();
    }
}