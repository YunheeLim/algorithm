def solution(phone_book):
    answer = True
    dic = {}
    phone_book.sort()
    for phone in phone_book:
        flag = True
        front = ""
        for s in phone:
            front += s
            if front in dic:
                answer = False
                flag = False
                break
        if flag == False:
            break
        dic[phone] = 1
    return answer