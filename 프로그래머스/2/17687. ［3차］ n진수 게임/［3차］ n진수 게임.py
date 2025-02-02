def change(num, base):
    alpha = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    string = ""
    if num == 0:
        return "0"
    else:
        while num:
            remains = num % base
            if remains >= 10:
                string = alpha[remains] + string
            else:
                string = str(remains) + string
            num //= base
        return string
        
        

def solution(n, t, m, p):
    answer = ''
    order = []
    num = 0
    while len(order) <= t * m:
        copy_num = num
        order.extend(list(change(copy_num, n)))
        num += 1
        
    while len(answer) < t:
        answer += order[p - 1]
        p += m
        
        
    return answer