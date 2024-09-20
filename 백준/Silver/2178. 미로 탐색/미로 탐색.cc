#include <iostream>
#include <queue>

using namespace std;

int n, m;
int graph[100][100];
int visited[100][100] = { 0 };
queue<pair<int,int>> q;

void bfs(int x, int y){
    q.push(make_pair(x, y));
    visited[x][y] = 1;

    while (!q.empty()) {
        int newX = q.front().first;
        int newY = q.front().second;
        q.pop();

        int dx[4] = {-1, 1, 0, 0};
        int dy[4] = {0, 0, -1, 1};

        for (int i = 0; i < 4; i++) {
            int nx = newX + dx[i];
            int ny = newY + dy[i];

            if (nx >=0 && nx < n && ny >= 0 && ny < m) {
                if (!visited[nx][ny] && graph[nx][ny] == 1) {
                    visited[nx][ny] = visited[newX][newY] + 1;
                    q.push(make_pair(nx, ny));
                }
            }
        }
    }
}

int main() {
    cin >> n >> m;

    for (int i = 0; i < n; i++) {
        string row;
        cin >> row;

        for (int j = 0; j < m; j++) {
            graph[i][j] = row[j] - '0';
        }
    }

    bfs(0, 0);
    
    cout << visited[n - 1][m - 1];

    return 0;
}