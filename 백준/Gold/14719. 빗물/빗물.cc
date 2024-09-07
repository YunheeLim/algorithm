#include <iostream>
#include <vector>
using namespace std;


int main() {

	int H, W;
	cin >> H >> W;
	vector<int> v(W);

	for (int i = 0; i < W; i++) {
		cin >> v[i];
	}

	int ans = 0;

	for (int i = 1; i < W - 1; i++) {
		int left = 0, right = 0, min;

		for (int j = 0; j < i; j++) {
			left = (left < v[j]) ? v[j] : left;
		}
		for (int k = W - 1; k > i; k--) {
			right = (right < v[k]) ? v[k] : right;
		}
		min = (left < right) ? left : right;
		
		if (min - v[i] >= 0)
			ans += min - v[i];
		else
			ans += 0;
	}

	cout << ans << '\n';


	return 0;
}