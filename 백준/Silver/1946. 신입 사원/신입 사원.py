import sys
input = sys.stdin.readline

t = int(input())

while t:
    n = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(n)]

    arr.sort()

    ans = 1
    top = 0

    for i in range(1, len(arr)):
        if arr[i][1] < arr[top][1]:
            top = i
            ans += 1
            
    print(ans)

    t -= 1