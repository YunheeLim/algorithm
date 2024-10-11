#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
    int answer = 0;
    
    // Step 1: Initialize student items with 1
    vector<int> student(n + 1, 1);
    
    // Step 2: Mark lost items
    for (auto elem : lost) {
        student[elem]--;
    }
    
    // Step 3: Mark reserve items
    for (auto elem : reserve) {
        student[elem]++;
    }
    
    // Step 4: Borrow items if necessary
    for (int i = 1; i <= n; i++) {
        if (student[i] == 0) {
            if (i - 1 > 0 && student[i - 1] == 2) {
                student[i - 1]--;
                student[i]++;
            } else if (i + 1 <= n && student[i + 1] == 2) {
                student[i + 1]--;
                student[i]++;
            }
        }
    }
    
    // Step 5: Count students with at least 1 item
    for (int i = 1; i <= n; i++) {
        if (student[i] > 0) answer++;
    }
    
    return answer;
}
