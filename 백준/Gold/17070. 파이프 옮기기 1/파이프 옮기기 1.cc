#include <iostream>
using namespace std;

int n;
int board[16][16];
int dp[3][16][16] = {0};

int main(){
    cin >> n;

    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            cin >> board[i][j];
        }
    }

    dp[0][0][1] = 1;

    for (int i = 2; i < n; i++){
        if (board[0][i] == 0){
            dp[0][0][i] = dp[0][0][i - 1];
        }
    }

    for (int r = 1; r < n; r++){
        for (int c = 1; c < n; c++){
            if (board[r][c] == 0 && board[r][c - 1] == 0 and board[r - 1][c] == 0){
                dp[1][r][c] = dp[0][r - 1][c - 1] + dp[1][r - 1][c - 1] + dp[2][r - 1][c - 1];
            }
            if (board[r][c] == 0){
                dp[0][r][c] = dp[0][r][c - 1] + dp[1][r][c - 1];
                dp[2][r][c] = dp[1][r - 1][c] + dp[2][r - 1][c];
            }
        }
    }

    int answer = dp[0][n - 1][n - 1] + dp[1][n - 1][n - 1] + dp[2][n - 1][n - 1];;

    cout << answer;

    return 0;
}