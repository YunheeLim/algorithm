#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int r, c;
char graph[20][20];
vector<char> history;
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};
int ans = 1;

void dfs(int x, int y, int cnt) {
    if (cnt > ans) ans = cnt;

    for (int i = 0; i < 4; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];

        if (nx >= 0 && nx < r && ny >=0 && ny < c) {
            auto exist = find(history.begin(), history.end(), graph[nx][ny]);
            if (exist == history.end()) {
                history.push_back(graph[nx][ny]);
                dfs(nx, ny, cnt + 1);
                history.pop_back();
            }
        }
    }
}

int main() {
    cin >> r >> c;

    for (int i = 0; i < r; i++) {
        string s;
        cin >> s;
        for (int j = 0; j < c; j++) {
            graph[i][j] = s[j];
        }
    }

    history.push_back(graph[0][0]);
    dfs(0, 0, 1);
    cout << ans;

    // for (int i = 0; i < r; i++) {
    //     for (int j = 0; j < c; j++) {
    //         cout << graph[i][j] << " ";
    //     }
    //     cout << endl;
    // }

    return 0;
}