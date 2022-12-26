#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <regex>

using namespace std;

int main()
{
    int matched = 0;
    regex r("(\\d+)-(\\d+) ([a-z]): (.+)");
    string line;
    vector<string> data;
    ifstream myfile("data.txt");
    if (myfile.is_open()) {
        while (getline(myfile, line)) {
            data.push_back(line);
        }
        myfile.close();

        smatch base_match;

        for (const auto &i : data)
        {
            if(regex_match(i, base_match, r)){
                int min = stoi(base_match[1].str());
                int max = stoi(base_match[2].str());
                char znak = base_match[3].str()[0];
                string str = base_match[4].str();
                int count = 0;

                if ((str[max - 1] == znak) != (str[min - 1] == znak))
                    matched++;
            }
        }
        cout << matched;

    }
    else
        cout << "Unable to open file";

    return 0;
}