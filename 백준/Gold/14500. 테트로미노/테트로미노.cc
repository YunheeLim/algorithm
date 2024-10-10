#include <iostream>
using namespace std;

int N, M;
int arr[500][500];
int visited[500][500] = { 0 };
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};
int ans = 0;

void dfs(int x, int y, int cnt, int sum) {
    if (cnt == 4) {
        ans = max(ans, sum);
        return;
    }

    for (int i = 0; i < 4; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];
        if (nx >= 0 && nx < N && ny >= 0 && ny < M) {
            if (!visited[nx][ny]) {
                visited[nx][ny] =  1;
                dfs(nx, ny, cnt + 1, sum + arr[nx][ny]);
                visited[nx][ny] = 0;
            }
        }
    }
}

void T(int x, int y) {
    for (int i = 0; i < 4; i++) {
        int sum = arr[x][y];
        int validCells = 0;

        for (int dir = 0; dir < 4; dir++) {
            if (dir == i) continue;
            int nx = x + dx[dir];
            int ny = y + dy[dir];
            if (nx >= 0 && nx < N && ny >= 0 && ny < M) {
                sum += arr[nx][ny];
                validCells++;
            } 
        }
        if (validCells == 3) ans = max(ans, sum);
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
            visited[i][j] = 1;
            dfs(i, j, 1, arr[i][j]);
            visited[i][j] = 0;
            T(i, j);

        }
    }

    cout << ans;

    return 0;

}