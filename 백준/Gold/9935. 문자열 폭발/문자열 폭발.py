string = input()
bomb = input()

stack = []
bomb_len = len(bomb)

for i in range(len(string)):
    stack.append(string[i])
    if ''.join(stack[-bomb_len:]) == bomb:
        for _ in range(bomb_len):
            stack.pop()

if stack == []:
    print("FRULA")
else:
    print(''.join(stack))