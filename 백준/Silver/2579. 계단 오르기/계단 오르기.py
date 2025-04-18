import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
arr = [0] + arr
dp = [0] * (n + 1)

# 초기화
dp[1] = arr[1]

if n >= 2:
    dp[2] = arr[1] + arr[2]

if n >= 3:
    # DP
    for i in range(3, n + 1):
        dp[i] = max(arr[i] + dp[i - 2],  arr[i] + arr[i - 1] + dp[i - 3])

print(dp[-1])