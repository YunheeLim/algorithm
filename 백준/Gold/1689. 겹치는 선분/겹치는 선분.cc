#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N;
vector<pair<int, int>> v;

int main() {
    cin >> N;

    for (int i = 0; i < N; i++) {
        int s, e;
        cin >> s >> e;
        v.push_back({s, 1});
        v.push_back({e, -1});
    }

    sort(v.begin(), v.end());

    int cnt = 0;
    int ans = 0;
    for (int i = 0; i < v.size(); i++) {
        cnt += v[i].second;
        if (cnt > ans) ans = cnt;
    }

    cout << ans;

    return 0;
}