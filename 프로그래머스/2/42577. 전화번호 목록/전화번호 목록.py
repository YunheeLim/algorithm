def solution(phone_book):
    answer = True
    dic = set()
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
        dic.add(phone)
    return answer