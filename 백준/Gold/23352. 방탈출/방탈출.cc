#include <iostream>
#include <queue>
#include <map>
using namespace std;

int N, M;
int arr[50][50];
int visited[50][50] = { 0 };
int len = 0;
int maxVal = 0;
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};
map<int, int> m;

void bfs(int x, int y) {
    visited[x][y] = 1;
    queue<pair<int, int>> q;
    q.push({x, y});
    int start = arr[x][y];

    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx >= 0 && nx < N && ny >= 0 && ny < M) {
                if (arr[nx][ny] && !visited[nx][ny]) {
                    visited[nx][ny] = visited[x][y] + 1;
                    if (len <= visited[nx][ny]) {
                        len = visited[nx][ny];
                        if (m.find(len) == m.end()) {
                             m.insert({len, start + arr[nx][ny]});
                        } else {
                            if (m[len] < start + arr[nx][ny]) {
                                m[len] = start + arr[nx][ny];
                            }
                        }
                    }
                    q.push({nx, ny});
                }
            }
        }
    }
}

int main() {
    cin >> N >> M;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cin >> arr[i][j];
        }
    }

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            if (arr[i][j] != 0) {
                bfs(i, j);
                for (int k = 0; k < N; k++) {
                    for (int l = 0; l < M; l++) {
                        visited[k][l] = 0;
                    }
                }
            }
        }
    }
    cout << m[len];

    return 0;

}