n, m = map(int, input().split())
arr = list(map(int, input().split()))

# 누적합 생성
prefix_sum = [0] * n
prefix_sum[0] = arr[0]
for i in range(1, n):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i]

for _ in range(m):
    i, j = map(int, input().split())
    if i == 1:
        print(prefix_sum[j - 1])
    else:
        print(prefix_sum[j - 1] - prefix_sum[i - 2])