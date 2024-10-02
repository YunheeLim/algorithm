import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

rank = []
rank.append(arr[0])

cnt = 1

for i in range(1, n):
    idx = 1
    draw = False

    for j in range(cnt):
        compare = 0

        if type(rank[j][0]) == list:
            compare = rank[j][1]
        else:
            compare = rank[j]
            if compare[0] == 0:
                continue

        if arr[i][1] > compare[1]:
            idx = j
        elif arr[i][1] == compare[1]:
            if arr[i][2] > compare[2]:
                idx = j
            elif arr[i][2] == compare[2]:
                if arr[i][3] > compare[3]:
                    idx = j
                elif arr[i][3] == compare[3]:
                    draw = True
                    idx = j
                    break
                else:
                    idx = j + 1
            else:
                idx = j + 1
        else:
            idx = j + 1

    if draw:
        temp = rank[idx]
        rank.insert(idx, [arr[i], temp])
  
        rank[idx + 1] = [0, -1, -1, -1]
        cnt += 1

    else:
        rank.insert(idx, arr[i])
        cnt += 1

#print('[rank]', rank)
for i in range(len(rank)):
    # print(rank[i])
    if type(rank[i][0]) == list:
        for j in range(len(rank[i])):
            if k == rank[i][j][0]:
                print(i+1)
                exit()
    else:
        if k == rank[i][0]:
            print(i+1)
            exit()