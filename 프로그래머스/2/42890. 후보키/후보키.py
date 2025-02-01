from itertools import combinations

def solution(relation):
    answer = 0
    lst = []
    
    col_count = len(relation[0])  # 컬럼 개수
    row_count = len(relation)  # 행 개수

    for i in range(1, col_count + 1):  # 1~컬럼 개수까지 조합 생성
        for combi in combinations(range(col_count), i):
            
            temp = set()
            for r in relation:
                key = tuple(r[idx] for idx in combi)  # 튜플 사용
                if key in temp:
                    break  # 중복 발견 시 종료
                temp.add(key)
            else:  # 유일성 만족하면 최소성 검사
                candidate = set(combi)
                if all(not set(l).issubset(candidate) for l in lst):
                    lst.append(candidate)
                    answer += 1
                    
    return answer
