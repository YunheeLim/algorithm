n, m = map(int, input().split())
nums = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(m)]
prefix_sum = [0]
sum = 0
for i in nums:
    sum += i
    prefix_sum.append(sum)
for i, j in arr:
    print(prefix_sum[j] - prefix_sum[i - 1])
