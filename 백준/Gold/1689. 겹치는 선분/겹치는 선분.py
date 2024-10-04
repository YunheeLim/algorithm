import sys
input = sys.stdin.readline

N = int(input().rstrip())
arr = []
for _ in range(N):
    a,b = map(int,input().rstrip().split())
    arr.append((a,1)) # 선분 시작
    arr.append((b,-1)) # 선분 끝

arr.sort()
tot = 0
cnt = 0

for _ , point in arr:
    cnt += point
    tot = max(tot,cnt)

print(tot)
