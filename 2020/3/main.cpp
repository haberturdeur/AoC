#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
    string line;
    vector<vector<bool>> data;

    ifstream myfile("data.txt");
    if (myfile.is_open()) {
        int yGet = 0;
        while (getline(myfile, line)) {
            int xGet = 0;
            data.resize(yGet+1);
            for (const auto& i : line) {
                if (i == '#')
                    data[yGet].push_back(1);
                else if (i == '.')
                    data[yGet].push_back(0);
                xGet++;
            }
            yGet++;
        }
        myfile.close();

        unsigned count = 1;
        unsigned count11 = 0;
        unsigned count13 = 0;
        unsigned count15 = 0;
        unsigned count17 = 0;
        unsigned count21 = 0;

        unsigned x = 0;
        for (auto &y : data)
        {
            count11 += y[x];
            x = (x + 1) % (y.size());
        }

        count *= count11; 

        x = 0;
        for (auto &y : data)
        {
            count13 += y[x];
            x = (x + 3) % (y.size());
        }

        count *= count13;

        x = 0;
        for (auto &y : data)
        {
            count15 += y[x];
            x = (x + 5) % (y.size());
        }

        count *= count15;

        x = 0;
        for (auto &y : data)
        {
            count17 += y[x];
            x = (x + 7) % (y.size());
        }

        count *= count17;
        x = 0;
        for (unsigned yA = 0; yA < data.size(); yA += 2)
        {
            count21 += data[yA][x];
            x = (x + 1) % (data[yA].size());
        }
        
        count *= count21;

        cout<<count;
        
    }
    else
        cout << "Unable to open file";

    return 0;
}