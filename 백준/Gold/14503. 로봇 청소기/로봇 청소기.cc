#include <iostream>
using namespace std;

int N, M, r, c, d;
int graph[50][50];
int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, 1, 0, -1};
int ans = 0;

void cleaning(int x, int y, int dir) {
    if (graph[x][y] == 0) {
        graph[x][y] = 2;
        ans++;
    }
    bool canClean = false;

    for (int i = 0; i < 4; i++) {
        int nx = x + dx[(dir + 3 - i) % 4];
        int ny = y + dy[(dir + 3 - i) % 4];
        if (nx >= 0 && nx < N && ny >= 0 && ny < M) {
            if (graph[nx][ny] == 0) {
                canClean = true;
                cleaning(nx, ny, (dir + 3 - i) % 4);
                return;
            }
        }
    }
    // 주변 청소 불가능
    if (!canClean) {
        int backDir = (dir + 2) % 4;
        int bx = x + dx[backDir];
        int by = y + dy[backDir];
        if (bx >= 0 && bx < N && by >= 0 && by < M && graph[bx][by] != 1){
            cleaning(x + dx[backDir], y + dy[backDir], dir);
        } 
    }
}

int main() {
    cin >> N >> M;
    cin >> r >> c >> d;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cin >> graph[i][j];
        }
    }
    cleaning(r, c, d);

    cout << ans;

    return 0;
}