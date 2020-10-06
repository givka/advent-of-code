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
    vector<string> strings;
    int index = str.find(c);
    strings.push_back(str.substr(0, index));
    strings.push_back(str.substr(index + 1));
    return strings;
}

void create_rect(vector<string> &command) {
    auto strings = split(command[1], 'x');
    int xx = stoi(strings[0]);
    int yy = stoi(strings[1]);

    for (int y = 0; y < yy; ++y) {
        for (int x = 0; x < xx; ++x) {
            map[y][x] = '#';
        }
    }
}

void rotate_column(vector<string> &command) {
    auto strings = split(command[2], '=');
    int where = stoi(strings[1]);
    int by = stoi(command[4]);

    vector<char> chars;
    for (int y = 0; y < HEIGHT; y++) {
        chars.emplace_back(map[(y - by + HEIGHT) % HEIGHT][where]);
    }

    for (int y = 0; y < HEIGHT; y++) {
        map[y][where] = chars[y];
    }
}

void rotate_row(vector<string> &command) {
    auto strings = split(command[2], '=');
    int where = stoi(strings[1]);
    int by = stoi(command[4]);

    vector<char> chars;
    for (int x = 0; x < WIDTH; x++) {
        chars.emplace_back(map[where][(x - by + WIDTH) % WIDTH]);
    }

    for (int x = 0; x < WIDTH; x++) {
        map[where][x] = chars[x];
    }
}

int main() {
    ifstream input("08.in");
    vector<vector<string>> commands;

    for (string line; getline(input, line);) {
        istringstream iss(line);
        vector<string> command;
        for (string word; getline(iss, word, ' ');) {
            command.push_back(word);
        }
        commands.push_back(command);
    }

    for (int y = 0; y < HEIGHT; ++y) {
        for (int x = 0; x < WIDTH; ++x) {
            map[y][x] = ' ';
        }
    }

    for (vector<string> &command : commands) {
        if (command[0] == "rect")
            create_rect(command);
        else if (command[1] == "column")
            rotate_column(command);
        else
            rotate_row(command);
    }

    int count = 0;

    PRINTLN();
    for (int y = 0; y < HEIGHT; ++y) {
        for (int x = 0; x < WIDTH; ++x) {
            if (map[y][x] == '#') {
                ++count;
            }
            PRINT(map[y][x]);
        }
        PRINTLN();
    }
    PRINTLN();

    PRINTLN(count);
}