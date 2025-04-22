import sys
input = sys.stdin.readline

str = input().rstrip()

stack = []
tmp = 0
answer = 0
for i in range(len(str)):
    if str[i] == "(":
        stack.append(str[i])
    else:
        if str[i - 1] == "(": # 레이저
            stack.pop()
            answer += len(stack)
        else:
            stack.pop()
            answer += 1
     
print(answer)