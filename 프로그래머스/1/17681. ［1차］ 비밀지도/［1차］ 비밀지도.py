def solution(n, arr1, arr2):
    answer = []
        
    for i in range(n):
        row1 = bin(arr1[i])[2:]
        row1 = "0" * (n - len(row1)) + row1
        row2 = bin(arr2[i])[2:]
        row2 = "0" * (n - len(row2)) + row2
        result = ""

        for j in range(n):
            if row1[j] == "1" or row2[j] == "1":
                result += "#"
            else:
                result += " "
        
        answer.append(result)
    return answer