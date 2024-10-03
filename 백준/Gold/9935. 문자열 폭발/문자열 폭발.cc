#include <iostream>
#include <vector>
using namespace std;

string s, bomb;
vector<char> stack;

int main() {
    cin >> s;
    cin >> bomb;

    for (int i = 0; i < s.length(); i++) {
        stack.push_back(s[i]);

        if (stack.size() >= bomb.length()) {
            bool included = true;
            for (int j = 0; j < bomb.length(); j++) {
                if (stack[stack.size() - bomb.length() + j] != bomb[j]) {
                    included = false;
                    break;
                }
            }

            if (included) {
                for (int j = 0; j < bomb.length(); j++) {
                    stack.pop_back();
                }
            }
        }
    }

    if (stack.empty()) {
        cout << "FRULA";
    } else {
        for (char c : stack) {
            cout << c;
        }
    }
    return 0;
}