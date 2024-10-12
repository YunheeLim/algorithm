#include <iostream>
// #include <algorithm>
#include <vector>
using namespace std;

int N;

int main() {
    cin >> N;

    vector<int> arr(N + 1, N);

    for(int i = 3; i <= N; i++) {
        if (int(i % 3) == 0) {
            arr[i] = int(i / 3);
        }
        if (int(i % 5) == 0) {
            arr[i] = int(i / 5);
        }
    }

    for(int i = 8; i <= N; i++) {
        if (arr[i - 3]) {
            arr[i] = min(arr[i], arr[i - 3] + 1);
        }
        if (arr[i - 5]) {
            arr[i] = min(arr[i], arr[i - 5] + 1);
        }
    }

    if (arr[N] == N) cout << -1;
    else cout << arr[N];

    return 0;
}