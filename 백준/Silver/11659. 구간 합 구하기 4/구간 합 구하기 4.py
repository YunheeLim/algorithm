import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr = [0] + arr
prefix_sum = [0] * (n + 1)

total = 0
for i in range(1, n + 1):
    total += arr[i]
    prefix_sum[i] = total

for _ in range(m):
    s, e = map(int, input().split())
    print(prefix_sum[e] - prefix_sum[s - 1])
