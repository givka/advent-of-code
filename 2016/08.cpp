#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;
#define PRINTLN(message) cout << message << endl;
#define PRINT(message) cout << message;

const int HEIGHT = 6;
const int WIDTH = 50;

char map[HEIGHT][WIDTH];

vector<string> split(const string &str, char c) {
    istringstream iss(str);
    vector<string> strings;
    for (string sub_str; getline(iss, sub_str, c);) {
        strings.push_back(sub_str);
    }
    return strings;
}

int main() {

    for (int y = 0; y < HEIGHT; ++y) {
        for (int x = 0; x < WIDTH; ++x) {
            map[y][x] = ' ';
        }
    }

    ifstream input("08.in");

    for (string line; getline(input, line);) {
        vector<string> command = split(line, ' '); 

        if (command[0] == "rect") {
            auto strings = split(command[1], 'x');
            int xx = stoi(strings[0]);
            int yy = stoi(strings[1]);

            for (int y = 0; y < yy; ++y) {
                for (int x = 0; x < xx; ++x) {
                    map[y][x] = '#';
                }
            }
        }
        else if (command[0] == "rotate") {
            auto strings = split(command[2], '=');
            int where = stoi(strings[1]);
            int by = stoi(command[4]);

            if (command[1] == "column") {
                vector<char> chars;
                for (int y = 0; y < HEIGHT; y++) {
                    chars.emplace_back(map[(y - by + HEIGHT) % HEIGHT][where]);
                }

                for (int y = 0; y < HEIGHT; y++) {
                    map[y][where] = chars[y];
                }
            }
            else {
                vector<char> chars;
                for (int x = 0; x < WIDTH; x++) {
                    chars.emplace_back(map[where][(x - by + WIDTH) % WIDTH]);
                }

                for (int x = 0; x < WIDTH; x++) {
                    map[where][x] = chars[x];
                }
            }
        }
    }

    int count = 0;

    for (int y = 0; y < HEIGHT; ++y) {
        for (int x = 0; x < WIDTH; ++x) {
            if (map[y][x] == '#') {
                ++count;
            }
            PRINT(map[y][x]);
        }
        PRINTLN("");
    }

    PRINTLN(count);
}