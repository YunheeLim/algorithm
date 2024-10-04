#include <iostream>
#include <stack>
using namespace std;

string s;
int n;
stack<char> st1, st2;

int main() {
    cin >> s;
    cin >> n;

    char command, num;

    for (int i = 0; i < s.length(); i++) {
        st1.push(s[i]);
    }

    while (n--) {
        cin >> command;
        
        if (command == 'L') {
            if (!st1.empty()) {
                st2.push(st1.top());
                st1.pop();
            }
        } else if (command == 'D') {
            if (!st2.empty()) {
                st1.push(st2.top());
                st2.pop();
            }
        } else if (command == 'B') {
            if (!st1.empty()) {
                st1.pop();
            }
        } else if (command == 'P') {
            cin >> num;
            st1.push(num);
        }
    }

    // st1에 있는 내용 출력
    while (!st1.empty()) {
        st2.push(st1.top());
        st1.pop();
    }

    // 결과 출력
    while (!st2.empty()) {
        cout << st2.top();
        st2.pop();
    }

    return 0;
}