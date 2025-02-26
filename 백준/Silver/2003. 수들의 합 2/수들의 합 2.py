n, m = map(int, input().split())
arr = list(map(int, input().split()))

end = 0
interval_sum = 0
ans = 0

for start in range(n):
    while interval_sum < m and end < n:
        interval_sum += arr[end]
        end += 1
    if interval_sum == m:
        ans += 1
    interval_sum -= arr[start]

print(ans)