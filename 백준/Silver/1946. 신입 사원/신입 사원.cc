#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int T, N;
vector<pair<int, int>> v;

int main() {
    cin >> T;
    while (T--) {
        cin >> N;

        v.clear();

        for (int i = 0; i < N; i++) {
            int a, b;
            cin >> a >> b;
            v.push_back({a, b});
        }

        sort(v.begin(), v.end());

        int ans = 1;
        int top = 0;

        for (int i = 1; i < N; i++) {
            if (v[i].second < v[top].second) {
                top = i;
                ans++;
            }
        }

        cout << ans << endl;
    }

    return 0;
}