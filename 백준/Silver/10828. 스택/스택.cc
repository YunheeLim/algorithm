#include <iostream>
using namespace std;

int N;
int stack[10001];
int cur = -1;

int main() {
    string command;
    cin >> N;


    while (N--){
        cin >> command;

        if (command == "push"){
            cur++;
            int num;
            cin >> num;
            stack[cur] = num;
        } else if (command == "pop") {
            if (cur == -1) {
                cout << -1 << endl;
            } else {
                cout << stack[cur] << endl;
                cur--;
            }
        } else if (command == "size") {
            cout << cur + 1 << endl;
        } else if (command == "empty") {
            if (cur != -1) {
                cout << 0 << endl;
            } else {
                cout << 1 << endl;
            }
        } else if (command == "top") {
            if (cur != -1) {
                cout << stack[cur] << endl;
            } else {
                cout << -1 << endl;
            }
        }
    }


    return 0;
}