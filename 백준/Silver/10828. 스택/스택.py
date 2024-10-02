import sys
input = sys.stdin.readline

n = int(input())

stack = []
cur = -1
while n:
    line = input().split()
    command = line[0]
    if len(line) > 1:
        num = int(line[1])

    if command == "push":
        stack.append(num)
        cur += 1

    elif command == "pop":
        if cur == -1:
            print(-1)
        else:
            print(stack[cur])
            stack.pop()
            cur -= 1

    elif command == "size":
        print(cur + 1)
    
    elif command == "empty":
        if cur != -1:
            print(0)
        else:
            print(1)

    elif command == "top":
        if cur != -1:
            print(stack[cur])
        else:
            print(-1)
    
    n -= 1