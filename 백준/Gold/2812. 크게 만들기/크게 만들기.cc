#include <iostream>
#include <string>
#include <vector>
using namespace std;

vector<char> stack;

string solution(string number, int k) {
    string answer = "";
    
    for (int i = 0; i < number.size(); i++) {
        while (stack.size() && stack[stack.size() - 1] < number[i] && k) {
            stack.pop_back();
            k--;
        }
        
        stack.push_back(number[i]);
    }
    
    while (k--) {
        stack.pop_back();
    }
    
    for (auto elem : stack) {
        answer += elem;
    }

    return answer;
}

int main() {
    int N, K;
    string s;

    cin >> N >> K;
    cin >> s;

    cout << solution(s, K);

    return 0;
}