import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

start, end = 0, n - 1
ans_val = [arr[0], arr[1]]
answer = abs(arr[0] + arr[1])

while start < end:
    two_val = arr[start] + arr[end]
    if abs(two_val) < answer:
        answer = abs(arr[start] + arr[end])
        ans_val = [arr[start], arr[end]]
        if answer == 0:
            break
    if two_val < 0:
        start += 1
    else:
        end -= 1

ans_val.sort()
print(*ans_val)