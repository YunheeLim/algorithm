from collections import defaultdict

def solution(N, stages):
    answer = []
    dic = defaultdict(int)
    for stage in stages:
        dic[stage] += 1
        
    dic = dict(sorted(dic.items(), reverse=True))
    total = 0
    fails = [0] * (N + 1)
    for key, val in dic.items():
        total += val
        fail = val / total
        fails[key-1] = fail
    fails.pop()
    sorted_list = []
    for idx, val in enumerate(fails):
        sorted_list.append((val, idx + 1))
    sorted_list.sort(key=lambda x: (-x[0], x[1]))
    answer = [idx for val, idx in sorted_list]
        
    
    return answer