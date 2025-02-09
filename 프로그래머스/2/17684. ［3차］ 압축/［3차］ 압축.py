def solution(msg):
    answer = []
    dic = {}
    
    # 사전 초기화
    for idx in range(ord('A'), ord('Z') + 1):
        dic[chr(idx)] = idx - 64
        
    end_idx = 26
    idx = 0
    while idx < len(msg):
        s_idx = idx            
        tmp = msg[idx]
        last = ""
        flag = False
        while s_idx < len(msg) - 1:
            s_idx += 1
            last = tmp
            tmp += msg[s_idx]
            if tmp not in dic:
                flag = True
                break
        end_idx += 1
        if flag:
            dic[tmp] = end_idx
            answer.append(dic[last])
        else:
            answer.append(dic[tmp])
        if s_idx == len(msg) - 1 and not flag:
            break
        idx += len(last)
        
        
    return answer