#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n;
    cin >> n;

    vector<vector<int>> board(n, vector<int>(n));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> board[i][j];
        }
    }

    // 3차원 dp 배열: [방향 정보, 행, 열]
    // 방향 정보: 가로 - 0, 대각선 - 1, 세로 - 2
    vector<vector<vector<int>>> dp(3, vector<vector<int>>(n, vector<int>(n, 0)));
    
    // 초기 상태
    dp[0][0][1] = 1;

    // 첫 행은 가로 이동의 경우만 존재함
    for (int i = 2; i < n; ++i) {
        if (board[0][i] == 0) {
            dp[0][0][i] = dp[0][0][i - 1];
        }
    }

    for (int r = 1; r < n; ++r) {
        for (int c = 1; c < n; ++c) {
            // 대각선 이동: 파이프의 끝 뿐만 아니라 위, 왼쪽도 벽이 없어야 함
            if (board[r][c] == 0 && board[r][c - 1] == 0 && board[r - 1][c] == 0) {
                dp[1][r][c] = dp[0][r - 1][c - 1] + dp[1][r - 1][c - 1] + dp[2][r - 1][c - 1];
            }
            // 가로/세로 이동
            if (board[r][c] == 0) {
                // 가로 이동: 이동하기 전 위치에서의 가로, 대각선 파이프 개수
                dp[0][r][c] = dp[0][r][c - 1] + dp[1][r][c - 1];
                // 세로 이동: 이동하기 전 위치에서의 세로, 대각선 파이프 개수
                dp[2][r][c] = dp[1][r - 1][c] + dp[2][r - 1][c];
            }
        }
    }

    // 결과 출력
    int result = dp[0][n - 1][n - 1] + dp[1][n - 1][n - 1] + dp[2][n - 1][n - 1];
    cout << result << endl;

    return 0;
}
