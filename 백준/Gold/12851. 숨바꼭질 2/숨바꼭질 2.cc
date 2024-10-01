#include <iostream>
# include <queue>
using namespace std;
#define MAX 100001

int N, K;
int arr[MAX] = { 0 };
int cnt, result;
queue<int> q;

void bfs(int n) {
    int cur;

    q.push(n);

    while (!q.empty()) {
        cur = q.front();
        q.pop();

        if (cur == K) {
            result = arr[cur];
            cnt += 1;
            continue;
        }

        for (int i : {cur - 1, cur + 1, cur * 2}) {
            if (i >= 0 && i < MAX && (arr[i] == 0 || arr[i] == arr[cur] + 1)) {
                arr[i] = arr[cur] + 1;
                q.push(i);
            }
        }
    }
}

int main() {
    cin >> N >> K;

    bfs(N);

    cout << result << endl << cnt;

    return 0;
}