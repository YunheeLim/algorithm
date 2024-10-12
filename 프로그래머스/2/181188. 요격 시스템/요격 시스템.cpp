#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

bool cmp(vector<int> v1, vector<int> v2) {
    if (v1[1] < v2[1]) {
        return true;
    } else if (v1[1] == v2[1]) {
        if (v1[0] <= v2[0]) {
            return true;
        }
    }
    return false;
}

int solution(vector<vector<int>> targets) {
    int answer = 0;

    sort(targets.begin(), targets.end(), cmp);
    
    int check = -1;
    
    for (int i = 0; i < targets.size(); i++) {
        if (targets[i][0] >= check) {
            answer++;
            check = targets[i][1];
        }
    }
    
    // for (auto elem : targets) {
    //     cout << elem[0] << ", " << elem[1] << endl;
    // }
    
    return answer;
}