#include <iostream>
#include <algorithm>
using namespace std;

int N, K;
int rank[1001][1001];

struct Country {
    int num;
    int gold;
    int silver;
    int bronze;
};

bool compare(Country country_a, Country country_b) {
       // 먼저 금메달을 비교
    if (country_a.gold > country_b.gold) {
        return true;
    } else if (country_a.gold < country_b.gold) {
        return false;
    }
    
    // 금메달이 같을 경우 은메달을 비교
    if (country_a.silver > country_b.silver) {
        return true;
    } else if (country_a.silver < country_b.silver) {
        return false;
    }
    
    // 은메달도 같을 경우 동메달을 비교
    if (country_a.bronze > country_b.bronze) {
        return true;
    } else if (country_a.bronze < country_b.bronze) {
        return false;
    }

    // 모든 메달 수가 같을 경우 false 반환
    return false;
}

int main() {
    cin >> N >> K;

    Country* countries = new Country[N];    

    for (int i = 0; i < N; i++) {
        cin >> countries[i].num >> countries[i].gold >> countries[i].silver >> countries[i].bronze;
    }

    sort(countries, countries + N, compare);

    int idx = -1;

    for (int i = 0; i < N; i++) {
        if (countries[i].num == K){
            idx = i;
        }
    }

    int ans = 1;

    for (int i = 0; i < N; i++) {
        if (countries[idx].gold == countries[i].gold && countries[idx].silver == countries[i].silver && countries[idx].bronze == countries[i].bronze) {
            cout << ans;
            break;
        }
        ans++;
    }

    return 0; 
}