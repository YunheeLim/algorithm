import sys
sys.stdin.readline

h, w = map(int, input().split())

arr = list(map(int, input().split()))

answer = 0

for i in range(1, w - 1):
    left_max = max(arr[:i])
    right_max = max(arr[i + 1: ])

    compare = min(left_max, right_max)

    if arr[i] < compare:
        answer += compare - arr[i]
    
print(answer)