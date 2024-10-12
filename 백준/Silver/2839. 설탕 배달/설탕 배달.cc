#include <iostream>
// #include <algorithm>
#include <vector>
using namespace std;

int N;
int ans = 0;

int main() {
    cin >> N;

    while (N) {
        if (N % 5 == 0) {
            ans += int(N / 5);
            break;
        }
        else {
            N -= 3;
            ans++;
        }
    }

    if (N < 0) cout << -1;
    else cout << ans;
 
    return 0;
}