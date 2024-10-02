def solution(n, words):
    answer = []

    current = []
    
    turn = 0
    
    if len(words[0]) > 1:
        current.append(words[0])
        
        while turn < len(words) - 1:
            turn += 1

            if words[turn][0] != current[-1][-1]:
                temp = (turn + 1) % n
                if temp == 0:
                    temp += n
                answer.extend([temp, turn // n + 1])
                break

            if words[turn] not in current:
                current.append(words[turn])
                
            else:
                temp = (turn + 1) % n
                if temp == 0:
                    temp += n
                answer.extend([temp, turn // n + 1])
                break
                
    else:
        answer.extend([1, 1])
    
    if not len(answer):
        answer.extend([0, 0])
        
    return answer