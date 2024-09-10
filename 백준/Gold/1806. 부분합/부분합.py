import sys
sys.stdin.readline

n, s = map(int, input().split())

arr = list(map(int, input().split()))

sum = 0
end = 0
ans = 100000

for start in range(n):
    
    while sum < s and end < n:
        sum += arr[end]
        end += 1

    if sum >= s:
        ans = min(ans, end - start)
    
    sum -= arr[start]

if ans == 100000:
    print(0)
else:
    print(ans)