n, m, k = map(int, input().split())

dp = [[1] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

if dp[n][m] < k:
    print(-1)
else:
    answer = ""
    while True:
        if n == 0 or m == 0:
            answer += "z" * m
            answer += "a" * n
            break
        
        split = dp[n - 1][m]
        if k <= split:
            answer += "a"
            n -= 1
        else:
            answer += "z"
            m -= 1
            k -= split
    print(answer)