#include <fstream>
#include <iostream>
#include <regex>
#include <string>
#include <vector>

using namespace std;

int main()
{

    regex regexes[] = {
        regex("hcl:#[0-9a-f]{6}(?=\\W)"),
        regex("ecl:(amb|blu|brn|gry|grn|hzl|oth)(?=\\W)"),
        regex("pid:\\d{9}(?=\\W)"),
        // regex("cid:.+?(?=[\\W])"),
    };

    ifstream myfile("message.txt");

    if (myfile.is_open()) {
        string line;
        vector<string> data;
        data.push_back(""); // vytvoří první prvek vektoru
        while (getline(myfile, line)) {
            if (line.size() > 0) // pokud řádek není prázdný == neodděluje záznamy:
                data.back() += line + " "; // přidej řádek k aktuálnímu záznamu
            else // pokud prázdný řádek == oddělování záznamů:
                data.push_back(""); // vytvoř nový záznam
        }
        myfile.close();

        for (auto& i : data)
            cout << i << endl; // debug výpis

        cout << "------------------------------------------------------------------" << endl;

        int counter = 0;
        for (auto& i : data) {
            int isOk = 1;
            int cislo = 0;
            smatch result;

            if (regex_search(i, result, regex("byr:(\\d{4})(?=[\\W])"))) {
                cislo = stoi(result.str(1));
                isOk *= ((1920 <= cislo) && (2002 >= cislo));
            } else
                isOk = 0;

            if (regex_search(i, result, regex("iyr:(\\d{4})(?=\\W)"))) {
                cislo = stoi(result.str(1));
                isOk *= ((2010 <= cislo) && (2020 >= cislo));
            } else
                isOk = 0;

            if (regex_search(i, result, regex("eyr:(\\d{4})(?=\\W)"))) {
                cislo = stoi(result.str(1));
                isOk *= ((2020 <= cislo) && (2030 >= cislo));
            } else
                isOk = 0;

            if (regex_search(i, result, regex("hgt:(\\d+)(cm|in)(?=\\W)"))) {
                cislo = stoi(result.str(1));
                if(result.str(2) == "in")
                    isOk *= ((59 <= cislo) && (76 >= cislo));
                else
                    isOk *= ((150 <= cislo) && (193 >= cislo));
            } else
                isOk = 0;

            for (auto& j : regexes) {
                isOk *= regex_search(i, j);
            }
            // cout << regex_search(i, j) << " "; // debug výpis

            counter += isOk;
            if (!isOk)
                cout << i << endl;
            // cout << endl;
        }
        cout << "Výsledek: " << counter << endl;
    } else
        cout << "Unable to open file!";
    return 0;
}
// byr (Birth Year) 4d 1920 <= x <= 2002
// iyr (Issue Year) 4d 2010 <= x <= 2020
// eyr (Expiration Year) 4d 2020 <= x <= 2030
// hgt (Height) ?d cm(150-193)/in(59-76)
// hcl (Hair Color) #[0-9a-f]{6}
// ecl (Eye Color) amb blu brn gry grn hzl oth
// pid (Passport ID) 9d

// cid (Country ID) - don't care