n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x: (x[1], x[0]))
end = 0
answer = 0
for s, e in arr:
    if s >= end:
        end = e
        answer += 1
print(answer)