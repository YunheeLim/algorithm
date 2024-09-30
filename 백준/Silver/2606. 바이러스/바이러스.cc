#include <iostream>
using namespace std;

int N, M, cnt = 0;
int arr[101][101] = { 0 };
bool mark[101] = { false };

void dfs(int c) {
	cnt++;
	mark[c] = true;
	for (int i = 1; i <= N; i++) {
		if (arr[c][i] == 1 && mark[i] == false) {
			dfs(i);
		}
	}
}

int main() {
	cin >> N;
	cin >> M;
	int c1, c2;
	for (int i = 0; i < M; i++) {
		cin >> c1 >> c2;
		arr[c1][c2] = 1;
		arr[c2][c1] = 1;
	}

	dfs(1);
	cout << cnt-1;

	return 0;
}