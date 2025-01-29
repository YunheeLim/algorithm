from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    answer = []

    for pick in course:
        comb_count = defaultdict(int)  # 조합 개수를 저장하는 딕셔너리
        
        # 1️⃣ 주문 내에서 조합 생성 후 카운트 증가
        for order in orders:
            sorted_order = sorted(order)  # 사전순 정렬하여 중복 방지
            for comb in combinations(sorted_order, pick):
                comb_count[comb] += 1

        # 2️⃣ 가장 많이 주문된 조합 찾기 (최소 2번 이상 등장)
        max_count = max(comb_count.values(), default=0)
        if max_count >= 2:
            for comb, count in comb_count.items():
                if count == max_count:
                    answer.append("".join(comb))  # 문자열로 변환하여 추가

    return sorted(answer)  # 최종 결과 정렬
