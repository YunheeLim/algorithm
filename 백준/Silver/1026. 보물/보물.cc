#include <iostream>
#include <algorithm>
using namespace std;

int N;
int A[50], B[50];

int main() {
    cin >> N;

    for (int i = 0; i < N; i++) {
        cin >> A[i];
    }
    for (int i = 0; i < N; i++) {
        cin >> B[i];
    }

    sort(A, A + N);
    sort(B, B + N, greater<int>());

    int ans = 0;

    for (int i = 0; i < N; i++) {
       ans += A[i] * B[i];
    }

    cout << ans;

    return 0;
}