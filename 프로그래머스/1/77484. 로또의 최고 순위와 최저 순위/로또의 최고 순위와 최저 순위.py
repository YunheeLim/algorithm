def ranking(cnt):
    if 7 - cnt > 5:
        return 6
    else:
        return 7 - cnt
    
def solution(lottos, win_nums):
    answer = []
    same = 0
    zero = 0
    for num in lottos:
        if num in win_nums:
            same += 1
        elif num == 0:
            zero += 1
    max_rank = ranking(same + zero)
    min_rank = ranking(same)
    
    answer.extend([max_rank, min_rank])
    
    return answer