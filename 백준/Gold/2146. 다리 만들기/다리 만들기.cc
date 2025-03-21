#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int N;
int arr[100][100];
int section[100][100];
bool visited[100][100];
int distances[100][100];
int answer = 10000;

// 나라 넘버링
void bfs(int x, int y, int country) {
    int dx[4] = {-1, 1, 0, 0};
    int dy[4] = {0, 0, -1, 1};

    queue<pair<int, int>> q;

    visited[x][y] = true;
    section[x][y] = country;
    q.push(make_pair(x, y));

    while (!q.empty()) {
        x = q.front().first;
        y = q.front().second;
        q.pop();
        
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx >= 0 && nx < N && ny >= 0 && ny < N) {

                if (arr[nx][ny] == 1 && visited[nx][ny] == false) {
                    visited[nx][ny] = true;
                    section[nx][ny] = country;
                    q.push({nx, ny});
                }
            }
        }
    }
    
}

// 다리 놓기
void make_bridge(int x, int y) {
    int dx[4] = {-1, 1, 0, 0};
    int dy[4] = {0, 0, -1, 1};

    queue<pair<int, int>> q;
    int start_country_num = section[x][y];

    q.push(make_pair(x, y));

    bool flag = false;

    while (!q.empty()) {
        x = q.front().first;
        y = q.front().second;
        q.pop();
        
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            
            if (nx >= 0 && nx < N && ny >= 0 && ny < N) {
                if (arr[nx][ny] == 0 && distances[nx][ny] == 0) {
                    distances[nx][ny] = distances[x][y] + 1;
                    q.push(make_pair(nx, ny));
                } 
                else if (arr[nx][ny] == 1 && section[nx][ny] != start_country_num && distances[nx][ny] == false) {
                    if (distances[x][y] < answer) {
                        answer = distances[x][y];
                    }
                }
            }
        }
    }
}

int main() {
    cin >> N;
    
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> arr[i][j];
            visited[i][j] = false;
            distances[i][j] = 0;
        }
    }

    int country = 0;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (arr[i][j] == 1 && visited[i][j] == false) {
                country++;
                bfs(i, j, country);
            }
        }
    }

    // 나라의 가장 자리일때만 자리 놓기 시작
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (arr[i][j] == 1) {
                make_bridge(i, j);
            }
            // 거리 정보 초기화
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    distances[i][j] = 0;
                }
            }
        }
    }

    cout << answer;

    // 나라 출력
    // for (int i = 0; i < N; i++) {
    //     for (int j = 0; j < N; j++) {
    //         cout << section[i][j] << " ";
    //     }
    //     cout << endl;
    // }



    // 배열 출력
    // for (int i = 0; i < N; i++) {
    //     for (int j = 0; j < N; j++) {
    //         cout << arr[i][j] << " ";
    //     }
    //     cout << endl;
    // }

    return 0;
}