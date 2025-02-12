import sys
import itertools
import collections

input = sys.stdin.readline

r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]

max_r, max_c = 3, 3  # 초기 크기 설정
ans = 0

while True:
    if 0 <= r - 1 < len(A) and 0 <= c - 1 < len(A[0]) and A[r - 1][c - 1] == k:
        print(ans)
        exit()

    if ans == 100:
        print(-1)
        exit()

    # R 연산 (행 연산)
    if len(A) >= len(A[0]):
        max_c = 0  # 새로운 최대 열 크기 갱신
        new_A = []
        
        for row in A:
            count_dict = collections.Counter(row)  # 숫자 빈도수 계산 (O(N))
            if 0 in count_dict:
                del count_dict[0]  # 0 제외
            
            sorted_row = sorted(count_dict.items(), key=lambda x: (x[1], x[0]))  # 빈도수 -> 숫자 순 정렬 (O(N log N))
            flat_row = list(itertools.chain.from_iterable(sorted_row))  # 펼치기
            
            max_c = max(max_c, len(flat_row))  # 최대 열 길이 갱신
            new_A.append(flat_row)
        
        # 0으로 길이 맞추기
        for row in new_A:
            row.extend([0] * (max_c - len(row)))
        
        A = new_A  # 행렬 업데이트

    # C 연산 (열 연산)
    else:
        max_r = 0  # 새로운 최대 행 크기 갱신
        cols = list(map(list, zip(*A)))  # 전치(transpose)
        new_cols = []
        
        for col in cols:
            count_dict = collections.Counter(col)  # 숫자 빈도수 계산 (O(N))
            if 0 in count_dict:
                del count_dict[0]  # 0 제외
            
            sorted_col = sorted(count_dict.items(), key=lambda x: (x[1], x[0]))  # 빈도수 -> 숫자 순 정렬 (O(N log N))
            flat_col = list(itertools.chain.from_iterable(sorted_col))  # 펼치기
            
            max_r = max(max_r, len(flat_col))  # 최대 행 길이 갱신
            new_cols.append(flat_col)
        
        # 0으로 길이 맞추기
        for col in new_cols:
            col.extend([0] * (max_r - len(col)))
        
        A = list(map(list, zip(*new_cols)))  # 다시 전치(transpose)하여 행렬 복원

    ans += 1

print(-1)
