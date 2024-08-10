n, m = map(int, input().split())
lst = list(map(int, input().split()))

start = 0
end = max(lst)

h = max(lst)

while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in lst:
        if x > mid:
            total += x - mid
    if total < m:
        end = mid - 1
    else:
        h = mid
        start = mid + 1


print(h)
        