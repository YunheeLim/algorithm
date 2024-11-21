import sys
input = sys.stdin.readline

n = int(input().rstrip())
c = list(map(int, input().rstrip().split()))
p = list(map(int, input().rstrip().split()))

ans = 0

for i in c:
    i -= p[0]
    if i:
        num = i // p[1]
        remain = i % p[1]
        if remain:
            ans += num + 2
        else:
            ans += num + 1
    else:
        ans += 1

print(ans)