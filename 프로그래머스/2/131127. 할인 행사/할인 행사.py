import copy

def solution(want, number, discount):
    answer = 0
    # 구매 품목 딕셔너리 생성
    dic = {}
    for goods, num in zip(want, number):
        dic[goods] = num
        
    start_idx = 0
    while start_idx + 10 <= len(discount):
        dic_copy = dic.copy()
        for idx in range(start_idx, start_idx + 10):
            item = discount[idx]
            if item in dic_copy and dic_copy[item] != 0:
                dic_copy[item] -= 1
                
        # 다 살 수 있는지 확인
        for k, v in dic_copy.items():
            if v != 0:
                break
        else:
            answer += 1
            
        start_idx += 1
        
    return answer