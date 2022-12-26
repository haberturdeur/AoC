#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

// vector<vector<int>> matrix = {
//     { 0, 1, 2 },
//     { 3, 4, 5 },
//     { 6, 7, 8 }
// };
// matrix[1][2] == 5

int main()
{
    string line;
    ifstream myfile("data.txt");

    vector<vector<bool>> map;

    if (myfile.is_open()) {
        for (int y = 0; getline(myfile, line); y++) {
            map.resize(y + 1);
            for (const auto& znak : line) {
                if (znak == '#') {
                    map[y].push_back(true);
                    // cout << true;
                } else {
                    map[y].push_back(false);
                    // cout << false;
                }
            }
            // cout << endl;
        }
        myfile.close();
    }

    int x = 0;
    int counter = 0;

    for (int y = 0; y < map.size(); y++) {
        if (map[y][x])
            counter++;

        x += 3;
        x %= map[y].size();
    }
    cout << counter << endl;
}

// Right 1, down 1.
// Right 3, down 1. (This is the slope you already checked.)
// Right 5, down 1.
// Right 7, down 1.

// Right 1, down 2.

// 1. Načíst data

// 1 0 1 0 1
// 0 1 1 0 1
