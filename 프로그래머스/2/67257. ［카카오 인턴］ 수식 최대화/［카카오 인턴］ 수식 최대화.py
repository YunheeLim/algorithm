from itertools import permutations
from collections import defaultdict
from copy import deepcopy

def solution(expression):
    answer = 0
    operand = set()
    count_dic = defaultdict(int)
    
    # 리스트에 쪼개기
    num = ""
    origin = []
    for s in expression:
        if s in "+-*":
            operand.add(s)
            count_dic[s] += 1
            origin.extend([num, s])
            num = ""
        else:
            num += s
    origin.append(num)
    
    for case in permutations(list(operand), len(operand)):
        split = []
        split[:] = origin[:]
        copy_dic = deepcopy(count_dic)
        for oper in case:
            while copy_dic[oper]:
                idx = split.index(oper)
                if oper == "+":
                    result = int(split[idx - 1]) + int(split[idx + 1])
                elif oper == "-":
                    result = int(split[idx - 1]) - int(split[idx + 1])
                else:
                    result = int(split[idx - 1]) * int(split[idx + 1])
                # print(oper,idx, result, split[idx-1], split[idx+1])
                split[idx - 1] = str(result)
                split[idx], split[idx + 1] = "", ""
                split = [v for v in split if v]
                copy_dic[oper] -= 1
        answer = max(answer, abs(int(split[0])))
    return answer