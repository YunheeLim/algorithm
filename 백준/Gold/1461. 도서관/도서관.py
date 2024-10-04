n, m = map(int, input().split())

arr = list(map(int, input().split()))
arr.append(0)
arr.sort()
origin = arr.index(0)
left = []
right = []
left = arr[:origin]
right = arr[origin + 1:]

last = 0
# 빈 리스트인 경우 예외 처리
if not len(left):
    last = right[-1]
elif not len(right):
    last = left[0]
else:

    if abs(left[0]) > right[-1]:
        last = left[0]
    else:
        last = right[-1]

ans = 0

if last < 0:
    while right:
        for i in range(m):
            if right:
                if i == 0:
                    ans += right[-1] * 2
                right.pop()

    left.reverse()
    while left:
        for i in range(m):
            if left:
                if i == 0:
                    if left[-1] == last:
                        ans += abs(left[-1])
                    else:
                        ans += abs(left[-1]) * 2
                left.pop()
else:
    left.reverse()
    while left:
        for i in range(m):
            if left:
                if i == 0:
                    ans += abs(left[-1]) * 2
                left.pop()
    while right:
        for i in range(m):
            if right:
                if i == 0:
                    if right[-1] == last:
                        ans += right[-1]
                    else:
                        ans += right[-1] * 2
                right.pop()

print(ans)