#include <iostream>
using namespace std;

int board[5][5];
int order[5][5];

void remove(int arr[][5], int num) {
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            if (num == arr[i][j]) {
                arr[i][j] = 0;
                return;
            } 
        }
    }
}

bool bingo(int arr[5][5]) {
    int cnt = 0;
    bool line = true;

    // 가로 확인
    for(int i = 0; i < 5; i++) {
        line = true;
        for(int j = 0; j < 5; j++) {
            if (arr[i][j] != 0) {
                line = false;
            }
        }
        if (line) cnt++;
    }

    // 세로 확인
    for(int i = 0; i < 5; i++) {
        line = true;
        for(int j = 0; j < 5; j++) {
            if (arr[j][i] != 0) {
                line = false;
            }
        }
        if (line) cnt++;
    }

    // 대각선 확인1
    line = true;
    for(int i = 0; i < 5; i++) {
        if (arr[i][i] != 0) {
            line = false;
        }
    }
    if (line) cnt++;

    // 대각선 확인2
    line = true;
    for(int i = 4; i >= 0; i--) {
        if (arr[i][4-i] != 0) {
            line = false;
        }
    }
    if (line) cnt++;

    return cnt >= 3;
}

int main() {
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            cin >> board[i][j];
        }
    }

    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            cin >> order[i][j];
        }
    }

    int ans = 0;

    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            ans++;
            int num = order[i][j];
            remove(board, num);
            if (bingo(board)) {
                cout << ans;
                return 0;
            }
        }
    }

    return 0;
}