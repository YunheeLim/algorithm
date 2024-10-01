#include <iostream>
#include <deque>
using namespace std;

#define MAX 100001

int N, K;
int arr[MAX] = { 0 };
deque<int> q;

int bfs(int cur, int target) {
    if (cur == 0) {
        q.push_back(1);
    } else {
        q.push_back(cur);
    }
    
    while (!q.empty()) {
        cur = q.front();
        q.pop_front();

        if (cur == target) {
            return arr[target];
        }

        for (int i: {cur - 1, cur + 1, cur * 2}) {
            if (i >= 0 && i < MAX && !arr[i]) {
                if (i == cur * 2) {
                    arr[i] = arr[cur];
                    q.push_front(i);
                } else {
                    arr[i] = arr[cur] + 1;
                    q.push_back(i);
                }
            }
        }
    }
}

int main() {
    cin >> N >> K;

    if (N == 0) {
        if (K == 0) {
            cout << 0;
        } else {
            cout << bfs(N, K) + 1;
        }
    } else {
        cout << bfs(N, K);
    }

    return 0;
}