import sys
input = sys.stdin.readline

n, k = map(int, input().split())
# 중복 동전 제거
coins = list(set([int(input()) for _ in range(n)]))

dp = [k+1] * (k + 1)
dp[0] = 0

for i in range(1, k + 1):
    for coin in coins:
        if i - coin >= 0:
            dp[i] = min(dp[i], dp[i-coin] + 1)
        
 
if dp[k] != k + 1:
    print(dp[k])
else:
    print(-1)
