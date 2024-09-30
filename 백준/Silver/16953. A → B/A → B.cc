#include <iostream>
using namespace std;

int a, b;

int main() {
    cin >> a >> b;

    int cnt = 1;
    int temp;
    int has_ans = 1;

    while (b != a) {
        cnt++;
        temp = b;

        if (b % 10 == 1) {
            b /= 10;
        } else if (b % 2 == 0) {
            b /= 2;
        }

        if (temp == b) {
            cout << -1;
            has_ans = 0;
            break;
        }
    }

    if (has_ans) {
        cout << cnt;
    }

    return 0;
}