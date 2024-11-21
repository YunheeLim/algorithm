import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
number = input().rstrip()
stack = []

for num in number:
    while stack and int(stack[-1]) < int(num) and k > 0:
        stack.pop()
        k -= 1
    stack.append(num)

if k > 0:
    print(''.join(stack[:-k]))
else:
    print(''.join(stack))