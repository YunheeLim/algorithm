import sys
sys.stdin.readline

n, m = map(int, input().split())

# n 명의 학생들의 우선순위를 저장하기 위한 리스트
arr = [0] * (n + 1)
# 비교된 적 있는 학생들 체크하는 리스트
visited = [0] * (n + 1)
# 특정 학생에 대해 자기보다 큰 학생들 저장하는 리스트
# 만약 compare[1]의 값이 [2,3]이라면 1번 학생보다 큰 학생들은 2번,3번 학생이라는 뜻
compare = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    # a보다 큰 학생 저장
    compare[a].append(b)
    # 비교된 학생들 체크
    visited[a] = 1
    visited[b] = 1
    # a학생의 우선순위가 b학생보다 크거나 같은 경우에만 우선순위 재정렬 필요
    if arr[a] >= arr[b]:
        arr[b] = arr[a] + 1
        
        if visited[b]:
            for higher in compare[b]:
                if higher != a:
                    arr[higher] += 1

for idx, val in enumerate(arr):
    arr[idx] = (val, idx)
arr.sort()

for i in range(1, len(arr)):
    if i == len(arr) -1:
        print(arr[i][1])
    else:
        print(arr[i][1], end=' ')
