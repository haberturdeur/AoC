#include <fstream>
#include <iostream>
#include <regex>
#include <string>
#include <vector>

using namespace std;

using Line = std::vector<int>;
using Board = std::vector<Line>;

struct Point {
    int x, y;
    Point(int _x, int _y)
        : x(_x)
        , y(_y)
    {
    }
};

struct Pipe {
    Point start;
    Point end;

    Pipe(Point _start, Point _end)
        : start(_start)
        , end(_end)
    {
    }
    void print() {
        cout << start.x << ", " << start.y << " -> " <<  end.x << ", " << end.y << endl;
    }
};

std::regex rege("(\\d+),(\\d+) -> (\\d+),(\\d+)");

int main()
{
    string line;
    vector<Pipe> data;
    ifstream myfile("data.txt");
    if (myfile.is_open()) {
        while (getline(myfile, line)) {
            std::smatch found;
            std::regex_search(line, found, rege);
            data.emplace_back(Pipe(Point(stoi(found[1].str()), stoi(found[2].str())), Point(stoi(found[3].str()), stoi(found[4].str()))));
            // data.back().print();
        }
        myfile.close();
        // cout << data.length();
    }

    Board board(1000, Line(1000, 0));
    for (auto& i : data) {
        if (i.start.x == i.end.x)
            for (int j = std::min(i.start.y, i.end.y); j <= std::max(i.start.y, i.end.y); j++)
                board.at(j).at(i.start.x) += 1;
        else if (i.start.y == i.end.y)
            for (int j = std::min(i.start.x, i.end.x); j <= std::max(i.start.x, i.end.x); j++)
                board.at(i.start.y).at(j) += 1;
        else if ((i.start.x > i.end.x && i.start.y > i.end.y) || (i.start.x < i.end.x && i.start.y < i.end.y))
            for (int j = 0; j <= std::max(i.start.x, i.end.x) - std::min(i.start.x, i.end.x); j++)
                board.at(std::min(i.start.y, i.end.y) + j).at(std::min(i.start.x, i.end.x)+j) += 1;
        else if (i.start.x < i.end.x)
            for (int j = 0; j <= i.end.x - i.start.x; j++)
                board.at(i.start.y - j).at(i.start.x + j) += 1;
        else
            for (int j = 0; j <= i.end.y - i.start.y; j++)
                board.at(i.start.y + j).at(i.start.x - j) += 1;
    }
    int count = 0;
    int y = 0;
    for (auto& i : board) {
        // std::cout << y << ": ";
        for (auto& j : i) {
            if (j >= 2)
                count++;
            // std::cout << j << " ";
        }
        // std::cout << std::endl;
        y++;
    }
    std::cout << count << std::endl;
}
