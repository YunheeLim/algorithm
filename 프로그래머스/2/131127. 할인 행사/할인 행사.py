def solution(want, number, discount):
    answer = 0
    start = 0

    while (start + 10 <= len(discount)):
        day = 0
        number_copy = number.copy()
        for i in range(start, start + 10):                
            day += 1

            if discount[i] in want:
                if number_copy[want.index(discount[i])]:
                    number_copy[want.index(discount[i])] -= 1
                    
        if (sum(number_copy) == 0):
            answer += 1
            
        start += 1
        
    return answer