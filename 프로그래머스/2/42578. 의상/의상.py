from collections import defaultdict

def solution(clothes):
    answer = 1
    dic = defaultdict(list)
    
    for cloth, category in clothes:
        dic[category].append(cloth)
                
    for key, val in dic.items():
        answer *= (len(val) + 1)    
    
    return answer - 1