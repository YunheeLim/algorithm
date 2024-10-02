import sys
input = sys.stdin.readline

n = int(input())

stack = []
cur = -1
while n:
    command = input().split()

    if command[0] == "push":
        stack.append(command[1])
        cur += 1

    elif command[0] == "pop":
        if cur == -1:
            print(-1)
        else:
            print(stack[cur])
            stack.pop()
            cur -= 1

    elif command[0] == "size":
        print(cur + 1)
    
    elif command[0] == "empty":
        if cur != -1:
            print(0)
        else:
            print(1)

    elif command[0] == "top":
        if cur != -1:
            print(stack[cur])
        else:
            print(-1)
    
    n -= 1