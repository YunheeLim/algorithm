#include <iostream>
#include <vector>
#include <stack>
using namespace std;

int N;

int main() {
    cin >> N;
    vector<int> v(N), place(N, -1);

    for (int i = 0; i < N; i++) {
        cin >> v[i];
    }
    
    stack<int> temp;

    for (int idx = 0; idx < N; idx++) {
        while(!temp.empty() && v[temp.top()] < v[idx]) {
            place[temp.top()] = v[idx];
            temp.pop();
        }
        temp.push(idx);
    }

    for (auto elem : place) {
        cout << elem << " ";
    }

    return 0;
}