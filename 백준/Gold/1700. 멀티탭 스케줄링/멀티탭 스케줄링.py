import sys

n, k = map(int, input().split())

arr = list(map(int, sys.stdin.readline().rstrip().split()))

plug = set()
cnt = 0

if n >= k:
    print(0)
    exit()

def find_latest(idx):
    result = 0
    max_idx = -1
    for num in plug:
        try:
            num_idx = arr[idx:].index(num)
        except:
            num_idx = k
        if max_idx < num_idx:
            result, max_idx = num, num_idx

    return result


for idx, num in enumerate(arr):
    plug.add(num)
    if len(plug) > n:
        cnt += 1
        latest_used = find_latest(idx)
        # set.discard()는 삭제할 요소가 없어도 에러발생 x
        plug.discard(latest_used)

print(cnt)