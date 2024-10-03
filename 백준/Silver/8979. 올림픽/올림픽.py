import sys
sys.stdin.readline

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
rank = []

for i in range(n):
    rank.append((arr[i][1] * 1000000**2 + arr[i][2] * 1000000 + arr[i][3], arr[i][0]))

rank.sort(reverse=True)

ans = 0
draw = 0
# print('[rank]', rank)

if rank[0][1] == k:
    print(1)
    exit()

for i in range(1, n):
    if rank[i][0] == rank[i-1][0]:
        draw += 1
    else:
        draw = 0

    if rank[i][1] == k:
        if draw:
            ans = i - draw
        else:
            ans = i
        break

print(ans + 1)