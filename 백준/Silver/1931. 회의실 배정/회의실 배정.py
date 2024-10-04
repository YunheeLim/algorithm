import sys
input = sys.stdin.readline

n = int(input())

arr = [tuple(map(int, input().split())) for _ in range(n)]

arr.sort(key = lambda x : (x[1], x[0]))

result = []
result.append(arr[0])

for i in range(1, n):
    if result[-1][1] > arr[i][0]:
        continue
    else:
        result.append(arr[i])

print(len(result))