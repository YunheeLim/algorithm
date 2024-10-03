#include <iostream>
#include <stack>
using namespace std;

string lines;
stack<char> s;

int main() {
    cin >> lines;

    int ans = 0;

    for (int i = 0; i < lines.size(); i++) {
        if (lines[i] == '(') {
            s.push('(');
        } else {
            if (lines[i - 1] == '(') {
                s.pop();
                ans += s.size();
            } else {
                s.pop();
                ans += 1;
            }
        }
    }

    cout << ans;

    return 0;
}