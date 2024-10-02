#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(int n, vector<string> words) {
    vector<int> answer;
    vector<string> current;
    
    int turn = 0;
    
    if (words[0].size() > 1) {
        current.push_back(words[0]);
        
        bool fail = false;
        
        while (turn < words.size() - 1) {
            turn++;
            int word_len = words[turn - 1].size();
            int current_len = words[turn].size();
            string last = words[turn - 1].substr(word_len - 1, word_len);
            string first = words[turn].substr(0, 1);
            
            if (last != first) {
                int temp = (turn + 1) % n;
                if (temp == 0) {
                    temp += n;
                }
                answer.push_back(temp);
                answer.push_back(turn / n + 1);
                fail = true;
                cout << "case 1: " << words[turn] << endl;
                break;
            }
            
            for (int i = 0; i < current.size(); i++) {
                if (current[i] == words[turn]) {
                    
                    int temp = (turn + 1) % n;
                    if (temp == 0) {
                        temp += n;
                    }
                    answer.push_back(temp);
                    answer.push_back(turn / n + 1);
                    fail = true;
                    cout << "case 2: " << words[turn] << endl;

                    break;
                }
            }
            if (fail) {
                break;
            }
            current.push_back(words[turn]);
        }
        
    } else {
        answer.push_back(1);
        answer.push_back(1);
    }
    
    if (!answer.size()) {
        answer.push_back(0);
        answer.push_back(0);
    }
    

    return answer;
}