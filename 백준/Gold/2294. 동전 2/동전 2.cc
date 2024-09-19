#include <iostream>
using namespace std;


int main(){
    int n, k;

    cin >> n >> k;

    int coins[n];
    int dp[10001];
    dp[0] = 0;

    for(int i = 0; i < n; i++){
        cin >> coins[i];
    }

    for(int i = 1; i < k + 1; i++){
        dp[i] = k + 1;
    }

    for(int i = 1; i < k + 2; i++){
        for(int j = 0; j < n; j++){
            if (i - coins[j] >= 0){
                if (dp[i] > dp[i - coins[j]]){
                    dp[i] = dp[i - coins[j]] + 1;
                }
            }
        }
    }

    if (dp[k] != k + 1){
        cout << dp[k];
    }else{
        cout << -1;
    }

    return 0;
}