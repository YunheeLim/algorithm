#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int N;
    vector<pair<int, int>> v;
    priority_queue<int, vector<int>, greater<int>> q;

    cin >> N;

    for (int i = 0; i < N; i++) {
        int s, t;
        cin >> s >> t;
        v.push_back({s, t});
    }

    sort(v.begin(), v.end());

    q.push(v[0].second);

    for (int i = 1; i < N; i++) {
        if (v[i].first < q.top()) {
            q.push(v[i].second);
        } else {
            q.pop();
            q.push(v[i].second);
        }
    }
    
    cout << q.size();

    return 0;
}