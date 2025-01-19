import math

def check(num_bin, prev_parent):
    mid = len(num_bin) // 2 # 루트 인덱스
    if num_bin:
        son = (num_bin[mid] == '1') # 자식 존재 여부
    else:
        return True
    
    if son and not prev_parent:
        return False
    else:
        return check(num_bin[mid + 1:], son) and check(num_bin[:mid], son)
        
    

def sol(num):
    if num == 1:
        return 1
    num_bin = bin(num)[2:]
    digit = 2 ** int(math.log(len(num_bin), 2) + 1) - 1
    num_bin = "0" * (digit - len(num_bin)) + num_bin
    
    if num_bin[len(num_bin) // 2] == '1' and check(num_bin, True):
        return 1
    else:
        return 0

def solution(numbers):
    answer = []
    for num in numbers:
        answer.append(sol(num))
    return answer