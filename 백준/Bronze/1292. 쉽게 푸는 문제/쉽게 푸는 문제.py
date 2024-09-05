import sys
sys.stdin.readline

a, b = map(int, input().split())

sequence = []
for i in range(1, 50):
    for _ in range(i):
        sequence.append(i)

result = 0
for i in range(a, b + 1):
    result += sequence[i - 1]

print(result)