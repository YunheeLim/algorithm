#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int N;

bool cmp(const pair<int, int>& a, const pair<int, int>& b) {
    if (a.second != b.second) 
        return a.second < b.second;
    else 
        return a.first < b.first;
}

int main() {
    cin >> N;
    vector<pair<int, int>> arr(N);
    vector<pair<int, int>> result;


    for (int i = 0; i < N; i++) {
        cin >> arr[i].first >> arr[i].second;
    }

    sort(arr.begin(), arr.end(), cmp);

    result.push_back(arr[0]);

    for (int i = 1; i < N; i++) {
        int last_idx = result.size()-1;
        if (arr[i].first >= result[last_idx].second) {
            result.push_back(arr[i]);
        } 
    }

    cout << result.size();

    return 0;
}
