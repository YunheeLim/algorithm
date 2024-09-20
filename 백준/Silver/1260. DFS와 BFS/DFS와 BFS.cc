#include <iostream>
#include <queue>
using namespace std;

int n, m, v;
int graph[1001][1001];
bool visited[1001];
queue<int> q;

void dfs(int start){
    visited[start] = true;
    cout << start << " ";
    for (int i = 1; i <= n; i++) {
        if (graph[start][i] == 1 && !visited[i]) {
            dfs(i);
        }
    }
}

void bfs(int start){
    q.push(start);
    visited[start] = true;
    while (!q.empty()) {
        int v = q.front();
        q.pop();
        cout << v << " ";
        for (int i = 1; i <= n; i++) {
            if (graph[v][i] == 1 and !visited[i]) {
                visited[i] = true;
                q.push(i);
            }
        }
    }
}

int main(){
    cin >> n >> m >> v;
    
    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        graph[a][b] = 1;
        graph[b][a] = 1;
    }

    for (int i = 0; i <= n; i++) {
        visited[i] = false;
    }

    dfs(v);

    for (int i = 0; i <= n; i++) {
        visited[i] = false;
    }

    cout << endl;

    bfs(v);

    return 0;
}