import sys
sys.setrecursionlimit(10000)

t = int(input())
n = int(input())

base = ["", "X", "YZ", "ZX"]  # base[1] ~ base[3]
dp = [0] * 101
cnt = [[0] * 3 for _ in range(101)]  # cnt[n][0]: X, [1]: Y, [2]: Z

# 초기값
dp[1] = 1
dp[2] = 2
dp[3] = 2
cnt[1][0] = 1  # X
cnt[2][1] = 1  # Y
cnt[2][2] = 1  # Z
cnt[3][0] = 1  # Z
cnt[3][2] = 1  # X

# DP 테이블 채우기
for i in range(4, n + 1):
    dp[i] = dp[i - 3] + dp[i - 2]
    for j in range(3):
        cnt[i][j] = cnt[i - 3][j] + cnt[i - 2][j]

# k번째 문자 찾기
def solve(idx, depth):
    if depth <= 3:
        return base[depth][idx - 1]
    if dp[depth - 3] >= idx:
        return solve(idx, depth - 3)
    else:
        return solve(idx - dp[depth - 3], depth - 2)

# 출력 처리
if t == 1:
    print(dp[n])
elif t == 2:
    k = int(input())
    print(solve(k, n))
else:
    ch = input().strip()
    print(cnt[n][ord(ch) - ord('X')])

