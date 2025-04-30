import sys
sys.setrecursionlimit(10000)

t = int(input())
n = int(input())

dp = [0] * 101
cnt = [[0, 0, 0] for _ in range(101)]
base = ["", "X", "YZ", "ZX"]

dp[1] = 1
dp[2] = 2
dp[3] = 2
cnt[1] = [1, 0, 0]
cnt[2] = [0, 1, 1]
cnt[3] = [1, 0, 1]

# 이분탐색으로 기저문자 찾기
def find(idx, depth):
    if depth <= 3:
        return base[depth][idx - 1]
    if dp[depth - 3] >= idx: # 왼쪽거
        return find(idx, depth - 3)
    else:
        return find(idx - dp[depth - 3], depth - 2)


for i in range(4, n + 1):
    dp[i] = dp[i - 3] + dp[i - 2]
    for j in range(3):
        cnt[i][j] = cnt[i - 3][j] + cnt[i - 2][j]

if t == 1:
    print(dp[n])
elif t == 2:
    k = int(input())
    print(find(k, n))
else:
    ch = input()
    print(cnt[n][ord(ch) - ord('X')])
