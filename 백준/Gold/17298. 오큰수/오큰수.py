import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
stack = []
place = [-1] * n

for idx in range(n):
    while stack and arr[stack[-1]] < arr[idx]:
        place[stack.pop()] = arr[idx]
    stack.append(idx)

print(*place)