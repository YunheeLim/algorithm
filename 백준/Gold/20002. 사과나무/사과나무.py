import sys
input = sys.stdin.readline

n = int(input())
arr = [[0] * (n + 1)]
for _ in range(n):
    arr.append([0]+list(map(int, input().split())))
prefix_sum = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    prefix_sum[i][1] = prefix_sum[i - 1][1] + arr[i][1]

for j in range(1, n + 1):
    prefix_sum[1][j] = prefix_sum[1][j - 1] + arr[1][j]

for i in range(2, n + 1):
    for j in range(2, n + 1):
        prefix_sum[i][j] = arr[i][j] + prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1]

# for e in prefix_sum:
#     print(e)
answer = -int(1e9)
for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            x1, y1, x2, y2 = i, j, i + k - 1, j + k - 1
            if x2 > n or y2 > n:
                continue
            total = prefix_sum[x2][y2] - prefix_sum[x1 - 1][y2] - prefix_sum[x2][y1 - 1] + prefix_sum[x1 - 1][y1 - 1]
            # print(total)
            answer = max(answer, total)
print(answer)