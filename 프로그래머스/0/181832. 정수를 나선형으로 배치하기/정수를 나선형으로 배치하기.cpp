#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<vector<int>> solution(int n) {
    vector<vector<int>> answer(n, vector<int>(n, 0));
    
    int num = 1;
    int cycle = 0;
    while (num <= n*n) {
        for (int i = 0; i < n; i++) {
            if (!answer[cycle][i]) {
                answer[cycle][i] = num;
                num++;
            }
        }

        for (int i = 0; i < n; i++) {
            if (!answer[i][n - 1 - cycle]) {
                answer[i][n - 1 - cycle] = num;
                num++;
            }
        }

        for (int i = n - 1; i >= 0; i--) {
            if (!answer[n - 1 - cycle][i]) {
                answer[n - 1 - cycle][i] = num;
                num++;
            }
        }
        
        for (int i = n - 1; i >= 0; i--) {
            if (!answer[i][cycle]) {
                answer[i][cycle] = num;
                num++;
            }
        }
        
        cycle++;
    }

    return answer;
}