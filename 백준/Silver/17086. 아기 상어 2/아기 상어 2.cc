#include <iostream>
#include <queue>
using namespace std;

int N, M;
int graph[51][51];
int visited[51][51] = { 0 };
queue<pair<int,int>> q;

void bfs(int r, int c) {
    q.push({r, c});

    int x, y, nx, ny;

    int dx[8] = {-1, -1, -1, 0, 0, 1, 1, 1};
    int dy[8] = {-1, 0, 1, -1, 1, -1, 0, 1};

    while (!q.empty()) {
        x = q.front().first;
        y = q.front().second;
        q.pop();

        for (int i = 0; i < 8; i++) {
            nx = x + dx[i];
            ny = y + dy[i];

            if (nx >= 0 && nx < N && ny >= 0 && ny < M) {
                if (graph[nx][ny] == 0 && (!visited[nx][ny] || visited[nx][ny] > visited[x][y] + 1)) {
                    visited[nx][ny] = visited[x][y] + 1;
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
            cin >> graph[i][j];
        }
    }

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            if (graph[i][j] == 1) {
                bfs(i, j);
            }
        }
    }

    int ans = -1;
    
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            if (ans < visited[i][j]) {
                ans = visited[i][j];
            }
        }
    }

    cout << ans;

    return 0;
}