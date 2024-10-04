#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
using namespace std;

bool cmp(pair<int, int> v1, pair<int, int> v2) {
    if (v1.first != v2.first) {
        return v1.first < v2.first;  // Sort by weight (ascending)
    }
    return v1.second > v2.second;    // If weights are the same, sort by value (descending)
}

int main() {

    int N, K;
    vector<pair<int, int>> jew;
    vector<int> bags;
    
    cin >> N >> K;

    for (int i = 0; i < N; i++) {
        int m, v;
        cin >> m >> v;
        jew.push_back({m, v});
    }

    for (int i = 0; i < K; i++) {
        int bag;
        cin >> bag;
        bags.push_back(bag);
    }

    sort(jew.begin(), jew.end(), cmp);  // Sort jewelry by weight, and by value if equal
    sort(bags.begin(), bags.end());     // Sort bags by capacity

    long long ans = 0;                  // Change to long long to avoid overflow
    priority_queue<int> temp_jew;       // Max heap for jewelry values

    int j = 0;                          // Index for jewelry
    for (int i = 0; i < K; i++) {
        // For each bag, add all jewelry that fits into the bag
        while (j < N && bags[i] >= jew[j].first) {
            temp_jew.push(jew[j].second);  // Push jewelry value into max heap
            j++;
        }
        // If there is any jewelry in the heap, take the one with the maximum value
        if (!temp_jew.empty()) {
            ans += temp_jew.top();
            temp_jew.pop();
        }
    }    
    cout << ans;

    return 0;
}
