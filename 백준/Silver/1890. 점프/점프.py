n = int(input())
array = [list(map(int,input().split())) for _ in range(n)]
m = len(array[0])
dp = [[0] * m for _ in range(n)]

dp[0][0] = 1

for i in range(n):
    for j in range(m):
        k = array[i][j]

        if k == 0 or array[i][j] == 0:
            continue

        if i + k < n:
            dp[i + k][j] += dp[i][j]
        if j + k < m:
            dp[i][j + k] += dp[i][j]

print(dp[-1][-1])