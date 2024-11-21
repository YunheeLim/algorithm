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
        remain = i % p[1]
        if remain:
            ans = max(ans, n * (num + 2))
        else:
            ans = max(ans, n * (num + 1))

print(ans)