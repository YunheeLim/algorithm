import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr = [0] + arr
dp = [0] * (n + 1)

for i in range(1, n + 1):
   dp[i] = max(dp[i], dp[i - 1]) # 현재는 항상 이전일보다 같거나 큼
   end_date = i + arr[i][0] - 1
   if end_date <= n:
     dp[end_date] = max(dp[end_date], dp[i - 1] + arr[i][1])

print(max(dp))