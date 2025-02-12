import sys
import itertools
input = sys.stdin.readline

r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]

max_r, max_c = 3, 3
ans = 0

while True:
    # A의 크기를 초과하지 않는지 확인
    if 0 <= r - 1 < len(A) and 0 <= c - 1 < len(A[0]) and A[r - 1][c - 1] == k:
        print(ans)
        exit()

    if ans == 100:
        print(-1)
        exit()

    # R 연산 (행 연산)
    if len(A) >= len(A[0]):
        new_A = []
        max_c = 0  # 새로운 최대 열 크기 갱신

        for i in range(len(A)):  # 기존 max_r이 아니라 실제 A 크기 사용
            nums = set(A[i])
            nums.discard(0)  # 0 제거
            new_row = [[s, A[i].count(s)] for s in nums]  # (숫자, 개수) 생성
            new_row.sort(key=lambda x: (x[1], x[0]))  # 개수 오름차순, 숫자 오름차순
            new_row = list(itertools.chain(*new_row))  # flatten

            max_c = max(max_c, len(new_row))  # 최대 열 길이 갱신
            new_A.append(new_row)

        # 0으로 길이 맞추기
        for row in new_A:
            row.extend([0] * (max_c - len(row)))

        A = new_A  # 업데이트

    # C 연산 (열 연산)
    else:
        cols = list(map(list, zip(*A)))  # 전치(transpose)
        new_cols = []
        max_r = 0  # 새로운 최대 행 크기 갱신

        for col in cols:
            nums = set(col)
            nums.discard(0)  # 0 제거
            new_col = [[s, col.count(s)] for s in nums]
            new_col.sort(key=lambda x: (x[1], x[0]))  # 개수 오름차순, 숫자 오름차순
            new_col = list(itertools.chain(*new_col))  # flatten

            max_r = max(max_r, len(new_col))  # 최대 행 길이 갱신
            new_cols.append(new_col)

        # 0으로 길이 맞추기
        for col in new_cols:
            col.extend([0] * (max_r - len(col)))

        A = list(map(list, zip(*new_cols)))  # 다시 전치(transpose)하여 행렬 복원

    ans += 1

print(-1)
