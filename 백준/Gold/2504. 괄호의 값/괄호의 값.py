import sys
sys.stdin.readline

arr = input()
stack = []

answer = 0
temp = 1

for i in range(len(arr)):
    if arr[i] == '(':
        stack.append(arr[i])
        temp *= 2
    elif arr[i] == '[':
        stack.append(arr[i])
        temp *= 3
    elif arr[i] == ')':
        if not stack or stack[-1] == '[':
            answer = 0
            break
        if arr[i - 1] == '(':
            answer += temp
        stack.pop()
        temp //= 2
    else:
        if not stack or stack[-1] == '(':
            answer = 0
            break
        if arr[i - 1] == '[':
            answer += temp
        stack.pop()
        temp //= 3

if stack:
    print(0)
else:
    print(answer)