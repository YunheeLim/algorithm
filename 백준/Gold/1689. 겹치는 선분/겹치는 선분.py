n = int(input())
arr = []
for _ in range(n):
    s, e = map(int, input().split())
    arr.append((s, 1))
    arr.append((e, -1))

answer = 0
arr.sort()
cnt = 0
for pos, event in arr:
    if event == 1:
        cnt += 1
    else:
        cnt -= 1
    answer = max(answer, cnt)
print(answer)

