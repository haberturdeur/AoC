#include <fstream>
#include <iostream>
#include <string>

using namespace std;

int main()
{
    int counter = 0;
    string line;
    ifstream myfile("data.txt");
    if (myfile.is_open()) {
        while (getline(myfile, line)) {
            int cursor = 0;
            string from = "";
            string to = "";
            string password = "";
            char character = 0;

            for (int i = 0; true; i++) {
                if (line[i] != '-')
                    from += line[i];
                else {
                    cursor = i + 1;
                    break;
                }
            }

            for (int i = cursor; true; i++) {
                if (line[i] != ' ')
                    to += line[i];
                else {
                    cursor = i + 1;
                    break;
                }
            }

            character = line[cursor];
            cursor += 3;

            password = line.substr(cursor);

            cout
                 << from << endl
                 << to << endl
                 << character << endl
                 << password << endl
                 << endl;
        }
        myfile.close();
    }
}

// 2-6 w: wkwwwfwwpvw
// 14-17 f: qfqffffqffnlwcffz

// int a = stoi(str);
