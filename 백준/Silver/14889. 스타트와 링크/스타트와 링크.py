import sys
from itertools import combinations
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
# 능력치 차이 최대로 초기화
answer = int(1e9)
# 사람 리스트
members = [i for i in range(n)]

for case in combinations(members, n // 2):
    team1 = list(case)
    team2 = []
    for mem in team1:
        # 반대 팀원
        team2 = [mem for mem in members if mem not in team1]

    s1 = 0
    s2 = 0
    for i in range(len(team1)):
        for j in range(i + 1, len(team1)):
            s1 += arr[team1[i]][team1[j]] + arr[team1[j]][team1[i]]
            s2 += arr[team2[i]][team2[j]] + arr[team2[j]][team2[i]]

    # 최솟값 갱신
    if abs(s1 - s2) < answer:
        answer = abs(s1 - s2)

print(answer)