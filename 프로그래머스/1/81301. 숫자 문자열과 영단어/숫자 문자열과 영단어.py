def solution(s):
    dic = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    answer = ""
    word = ""
    for c in s:
        word += c
        if word in dic:
            answer += dic[word]
            word = ""
        if c in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            answer += c
            word = ""

    
    return int(answer)