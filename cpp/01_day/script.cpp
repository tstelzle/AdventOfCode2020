#include <fstream>
#include <vector>
#include <string>
#include <iostream>

using namespace std;

vector<string> read_data(string filename) {
    ifstream myFile(filename);
    string line;

    vector<string> result;

    if(myFile.is_open()) {
        while (getline(myFile, line)) {
            result.push_back(line);
        }
    }
    myFile.close();

    return result;
}

int print_vector(vector<string> input) {
    vector<string>::iterator it = input.begin();

    while(it != input.end()) {
        cout << *it << "\n";
        it++;
    }

    return 0;
}

int main(int argc, char* argv[]) {
    vector<string> result = read_data("./data.txt");
    print_vector(result);

    return 0;
}