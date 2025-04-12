T = int(input())
test_case = [list(map(int, input().split())) for _ in range(T)]

def solution(arr):
    answer = 0
    for i in range(len(arr)):
        if arr[i] % 2 == 1:
            answer += arr[i]
    return answer

cnt = 1
for test in test_case:
    print(f"#{cnt} {solution(test)}")
    cnt += 1