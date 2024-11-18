from itertools import permutations

def solution(k, dungeons):
    answer = -1
    for i in permutations(dungeons, len(dungeons)):
        k_copy = k
        result = 0
        for j in i:
            if (k_copy >= j[0]):
                k_copy -= j[1]
                result += 1
                if (answer < result):
                    answer = result
            
    return answer