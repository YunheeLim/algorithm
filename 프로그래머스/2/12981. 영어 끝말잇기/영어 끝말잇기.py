def solution(n, words):
    answer = [0, 0]
    history = set()
    history.add(words[0]) # 맨 처음 넣고 시작
    turn = 1
    person = 1
    while person < len(words):
        print(turn, person % n)
        
        # 이어지는지
        print("current:", words[person][0])
        print("prev:", words[(person + (n - 1)) % n][-1])
        if words[person][0] != words[person - 1][-1]:
            return [person % n + 1, turn]
        # 나왔던 단어인지
        if words[person] in history:
            return [person % n + 1, turn]
        
        history.add(words[person])
        print(history)
        person += 1
        if person % n == 0: # 한 바퀴 돎
            turn += 1
            
    return answer