def solution(files):
    answer = []
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    split = []
    
    # HEAD, NUMBER, TAIL 분리
    for f_idx, file in enumerate(files):
        head = ""
        number = ""
        tail_sidx = -1
        isNum = False  
        for idx, c in enumerate(file):
            if len(number) == 0 and c not in numbers:
                head += c      
            if c in numbers:
                isNum = True
                if len(number) > 5:
                    tail_sidx = idx
                    break
                number += c
            if isNum and c not in numbers:
                tail_sidx = idx
                break
        split.append([f_idx, head.lower(), int(number), file[tail_sidx:]])
    
    split.sort(key = lambda x: (x[1], x[2]))
    
    for s in split:
        answer.append(files[s[0]])
    

    return answer