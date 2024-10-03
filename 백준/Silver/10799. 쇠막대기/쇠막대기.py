lines = input()
stack = []

ans = 0

for i in range(len(lines)):
    if lines[i] == '(':
        stack.append('(')
    else:
        if lines[i - 1] == '(':
            stack.pop()
            ans += len(stack)
        else:
            stack.pop()
            ans += 1

print(ans)