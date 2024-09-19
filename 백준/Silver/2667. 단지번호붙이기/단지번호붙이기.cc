#include <iostream>
#include <string>

using namespace std;

const int MAX_N = 25; // Assuming the maximum grid size is 25x25
int n;
string graph[MAX_N];
bool visited[MAX_N][MAX_N];

int dfs(int x, int y) {
    visited[x][y] = true;
    int count = 1; // Count this cell
    int dx[] = {-1, 1, 0, 0};
    int dy[] = {0, 0, -1, 1};

    for (int i = 0; i < 4; ++i) {
        int nx = x + dx[i];
        int ny = y + dy[i];
        if (nx >= 0 && nx < n && ny >= 0 && ny < n && !visited[nx][ny] && graph[nx][ny] == '1') {
            count += dfs(nx, ny);
        }
    }
    return count;
}

int main() {
    cin >> n;
    for (int i = 0; i < n; ++i) {
        cin >> graph[i];
    }

    int aptSizes[MAX_N * MAX_N]; // Maximum possible number of apartments
    int aptCount = 0;

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (graph[i][j] == '1' && !visited[i][j]) {
                aptSizes[aptCount] = dfs(i, j);
                aptCount++;
            }
        }
    }

    // Sort the sizes (simple bubble sort)
    for (int i = 0; i < aptCount; ++i) {
        for (int j = 0; j < aptCount - 1; ++j) {
            if (aptSizes[j] > aptSizes[j + 1]) {
                int temp = aptSizes[j];
                aptSizes[j] = aptSizes[j + 1];
                aptSizes[j + 1] = temp;
            }
        }
    }

    cout << aptCount << endl; // Number of connected components
    for (int i = 0; i < aptCount; ++i) {
        cout << aptSizes[i] << endl; // Size of each connected component
    }

    return 0;
}
