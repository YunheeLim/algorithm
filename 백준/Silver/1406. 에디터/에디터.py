import sys
input = sys.stdin.readline

st1 = list(input().rstrip())
n = int(input())

st2 = []

for _ in range(n):
    command = input().split()
    
    if command[0] == 'L':
        if st1:
            st2.append(st1.pop())

    elif command[0] == 'D':
        if st2:
            st1.append(st2.pop())

    elif command[0] == 'B':
        if st1:
            st1.pop()

    elif command[0] == 'P':
        st1.append(command[1])
    
st1.extend(reversed(st2))
print(''.join(st1))