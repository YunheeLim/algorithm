#include <iostream>
#include <queue>
using namespace std;

int N, M, K;
int graph[100][100] = { 0 };
int visited[100][100] = { 0 };
queue<pair<int, int>> q;

void bfs(int r, int c) {
    q.push({r, c});
    visited[r][c] = 1;

    int cnt = 1;

    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();

        int dx[4] = {-1, 1, 0, 0};
        int dy[4] = {0, 0, -1, 1};

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx >= 0 and nx < N and ny >= 0 and ny < M) {
                if (graph[nx][ny] == 1 && !visited[nx][ny]) {
                    cnt++;
                    visited[nx][ny] = cnt;
                    q.push({nx, ny});
                }
            }
        }
    }
}

int main() {
    cin >> N >> M >> K;

    for (int i = 0; i < K; i++) {
        int r, c;
        cin >> r >> c;
        graph[r - 1][c - 1] = 1;
    }


    for (int i = 0; i < N; i++){
        for (int j = 0; j < M; j++) {
            if (graph[i][j] == 1 && !visited[i][j]) {
                bfs(i, j);
            }
        }
    }

    int ans = 0;

    for (int i = 0; i < N; i++){
        for (int j = 0; j < M; j++) {
            if (visited[i][j] > ans) {
                ans = visited[i][j];
            }
        }
    }

    cout << ans;
    
    return 0;
}