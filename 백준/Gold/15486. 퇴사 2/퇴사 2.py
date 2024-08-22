import sys
input = sys.stdin.readline

n = int(input())

# i일까지의 최대 수익을 저장하는 dp 배열
dp = [0] * (n + 1)

schedule = [list(map(int, input().split())) for _ in range(n)]

# 현재까지의 수익
profit = 0

for i in range(n):
    # 현재 일수(i)까지의 최대 수익
    profit = max(profit, dp[i])

    # 상담일자 종료일이 퇴사일 이후인 경우
    if i + schedule[i][0] > n:
        continue

    # 상담 종료 일자의 현재값과 갱신할 값 비교 후 큰 값 저장
    dp[i + schedule[i][0]] = max(profit + schedule[i][1], dp[i + schedule[i][0]])

print(max(dp))
