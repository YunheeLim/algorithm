#include <iostream>
#include <queue>
using namespace std;

int N;
int dist[1001][1001] = { false };
queue<pair<int,int>> q;

void bfs() {
    dist[1][0] = 0;
    q.push({1, 0});

    int s, c;

    while (!q.empty()) {
        s = q.front().first;
        c = q.front().second;
        q.pop();

        if (dist[s][s] == false) {
            dist[s][s] = dist[s][c] + 1;
            q.push({s, s});
        }
        if (s + c <= N && dist[s + c][c] == false) {
            dist[s + c][c] = dist[s][c] + 1;
            q.push({s + c, c});
        }
        if (s - 1 >= 0 && dist[s - 1][c] == false) {
            dist[s - 1][c] = dist[s][c] + 1;
            q.push({s - 1, c});
        }
    }
}

int main() {
    cin >> N;

    bfs();

    int ans = -1;

    for (int j = 0; j <= N; j++) {
        if (dist[N][j] != false) {
            if (ans == -1 || ans > dist[N][j]) {
                ans = dist[N][j];
            }
        }
    }

    cout << ans;

    return 0;
}