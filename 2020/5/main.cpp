#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <cstdint>
#include <algorithm>

using namespace std;

int main()
{
    union Seat{
        struct {
            uint16_t id : 10;
            uint16_t reserved : 6;
        };
        struct
        {
            uint16_t column : 3;
            uint16_t row : 7;
            uint16_t reserved1 : 6;
        };
    };
    
    string line;
    vector<Seat> data;
    uint16_t maxID = 0;
    uint16_t sum = 0;
    ifstream myfile("data.txt");
    if (myfile.is_open()) {
        while (getline(myfile, line)) {
            for (auto &znak : line)
            {
                if (znak == 'B' || znak == 'R')
                    znak = '1';
                else
                    znak = '0';
            }
            Seat a;
            a.id = (uint16_t)stoi(line,0,2);
            data.push_back(a);
            maxID = max(maxID, a.id);
            // cout << maxID << endl;
        }
        myfile.close();
        sort(data.begin(), data.end(), [](Seat& first, Seat& second){
            return first.id < second.id;
        });

        uint16_t prev = data.front().id;
        for (int i = 1; i < data.size(); i++)
        {
            if ((data[i].id - 1) != prev){
                cout << i << " : " << data[i-1].id << ", " << data[i].id << endl;
            }
            prev = data[i].id;
        }
        
    } else
        cout << "Unable to open file";
    return 0;
}
// 0 1

// 0 63
// 0 31
// 0 15
// 0 7
// 0 3
// 0 1

// B, R....1
// F, L....0

// BFFFBBF RRR 70, 7 = 567
// 1000110 111

// 107

// 7 * 10^0 (1)
// 0 * 10^1 (10)
// 1 * 10^2 (100)

// 0b11010110

// 1 * 2^0 (1) - 1
// 1 * 2^1 (2) - 2
// 0 * 2^2 (4) - 0
// 1 * 2^3 (8) - 8
// 0 * 2^4 (16)- 0
// 1 * 2^5 (32)- 32
// 1 * 2^6 (64)- 64
