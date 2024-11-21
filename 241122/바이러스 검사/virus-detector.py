import sys
input = sys.stdin.readline

n = int(input().rstrip())
c = list(map(int, input().rstrip().split()))
p = list(map(int, input().rstrip().split()))

ans = 1

for i in c:
    i -= p[0]
    if i:
        num = i // p[1]
        remain = i % p[1] * num
        ans = max(ans, num + remain + 1)

print(ans * n)