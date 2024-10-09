#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

bool isFindAll(vector<int> number) {
    for (auto elem : number) {
        if (elem != 0) return false;
    }
    return true;
}

int solution(vector<string> want, vector<int> number, vector<string> discount) {
    int answer = 0;
    vector<string> origin_want = want;
    vector<int> origin_number = number;
    
    for(int start = 0; start < discount.size() - 9; start++) {
        want = origin_want;
        number = origin_number;
        for(int i = start; i < start + 10; i++) {
            auto it = find(want.begin(), want.end(), discount[i]);
            if (it != want.end()) {
                number[it - want.begin()]--;
                if (number[it - want.begin()] == 0) {
                    want[it - want.begin()] = "";
                }
            }
        }

        if (isFindAll(number)) answer++;

    }
    
    return answer;
}