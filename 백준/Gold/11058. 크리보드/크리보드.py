import sys
sys.stdin.readline

n = int(input())

dp = [i for i in range(n + 1)]

buffer = 1

for i in range(1, n + 1):
    buffer = dp[i]
    temp = 0
    for j in range(i + 3, n + 1):
        temp += buffer
        dp[j] = max(dp[j], dp[i] + temp)

print(dp[-1])