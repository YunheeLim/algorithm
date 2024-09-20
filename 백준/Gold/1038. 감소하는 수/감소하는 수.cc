#include <iostream>
#include <vector>
#include <queue>
using namespace std;

vector<long long> v;

void desc(int target) {
    queue<long long> q;
    for(int i = 0; i <= 9; i++){
        q.push(i);
        v.push_back(i);
    }
    while (!q.empty()) {
        long long num = q.front();
        int last = num % 10;
        q.pop();
        for (int i = 0; i < last; i++){
            long long newNum = num * 10 + i;
            q.push(newNum);
            v.push_back(newNum);
        }
    }
    if (target >= v.size()){
        cout << -1;
    }else {
        cout << v[target];
    }
}

int main(){
    int n;
    cin >> n;
    desc(n);
    return 0;
}