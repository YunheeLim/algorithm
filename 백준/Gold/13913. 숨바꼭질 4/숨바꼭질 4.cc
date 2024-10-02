#include <iostream>
#include <queue>
using namespace std;
#define MAX 100001

int N, K;
int t[MAX] = { 0 };
int path[MAX] = { 0 };
queue<int> q;

void print_path(int k) {
    int result[t[k] - 1];
    int temp = k;
    for (int i = 0; i < t[k] + 1; i++) {
        result[i] = temp;
        temp = path[temp];
    }
    for (int i = t[k]; i >= 0; i--) {
        cout << result[i] << " ";
    }
}

void bfs(int cur, int k) {
    q.push(cur);

    while (!q.empty()) {
        cur = q.front();
        q.pop();

        if (cur == k) {
            cout << t[k] << endl;
            print_path(k);
            break;
        }

        for (int i : {cur - 1, cur + 1, cur * 2}) {
            if (i >= 0 && i < MAX && !t[i]) {
                t[i] = t[cur] + 1;
                q.push(i);
                path[i] = cur;
            } 
        }
    }
}

int main() {
    cin >> N >> K;

    bfs(N, K);

    return 0;
}