q = int(input())
n = int(input())

dp = [0] * 101
dp[1] = 1
dp[2] = 2
dp[3] = 2

cnt = [[0, 0, 0] for _ in range(101)]
cnt[1] = [1, 0, 0]
cnt[2] = [0, 1, 1]
cnt[3] = [1, 0, 1]

# 1, 3번
for i in range(4, n + 1):
    dp[i] = dp[i - 3] + dp[i - 2]
    for j in range(3):
        cnt[i][j] = cnt[i - 3][j] + cnt[i - 2][j]

# 2번
base = ["", "X", "YZ", "ZX"]
def find(idx, depth):
    if depth <= 3:
        return base[depth][idx - 1]
    if idx <= dp[depth - 3]: # 왼쪽에서 옴
        return find(idx, depth - 3)
    else: # 오른쪽에서 옴
        return find(idx - dp[depth - 3], depth - 2)

if q == 1:
    print(dp[n])
elif q == 2:
    k = int(input())
    print(find(k, n))
else:
    ch = input()
    print(cnt[n][ord(ch)-ord('X')])