#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int parent[10001];
int v, e;
vector<pair<int, pair<int, int>>> edges;
int result = 0;

// 부모 찾기
int findParent(int x) {
    if (x == parent[x]) return x;
    return parent[x] = findParent(parent[x]);
}

// 부모 합치기
void unionParent(int a, int b) {
    a = findParent(a);
    b = findParent(b);
    if (a < b) {
        parent[b] = a;
    } else {
        parent[a] = b;
    }
}

int main() {
    cin >> v >> e;

    // 부모를 자기 자신으로 초기화
    for (int i = 1; i <= v; i++) {
        parent[i] = i;
    }

    // 간선 정보 입력
    for (int i = 0; i < e; i++) {
        int a, b, cost;
        cin >> a >> b >> cost;
        edges.push_back({cost, {a, b}});
    }

    sort(edges.begin(), edges.end());

    for (int i = 0; i < e; i++) {
        int a, b, cost;
        cost = edges[i].first;
        a = edges[i].second.first;
        b = edges[i].second.second;

        if (findParent(a) != findParent(b)) {
            unionParent(a, b);
            result += cost;
        }
    }

    cout << result;

    return 0;
}