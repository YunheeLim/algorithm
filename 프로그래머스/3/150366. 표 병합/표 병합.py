def solution(commands):
    answer = []
    table = [["EMPTY"] * 50 for _ in range(50)]
    merged = [[(i,j) for j in range(50)] for i in range(50)]
    
    for command in commands:
        com = command.split()
        if com[0] == "UPDATE":
            if len(com) == 4:
                r, c, value = int(com[1]) - 1, int(com[2]) - 1, com[3]
                x, y = merged[r][c]
                table[x][y] = value
            else:
                value1, value2 = com[1], com[2]
                for i in range(50):
                    for j in range(50):
                        if table[i][j] == value1:
                            table[i][j] = value2
                            
        elif com[0] == "MERGE":
            r1, c1, r2, c2 = int(com[1]) - 1, int(com[2]) - 1, int(com[3]) - 1, int(com[4]) - 1,
            x1, y1 = merged[r1][c1]
            x2, y2 = merged[r2][c2]
            if table[x1][y1] == "EMPTY":
                table[x1][y1] = table[x2][y2]
            for i in range(50):
                for j in range(50):
                    if merged[i][j] == (x2, y2):
                        merged[i][j] = (x1, y1)
                        
        elif com[0] == "UNMERGE":
            r, c = int(com[1]) - 1, int(com[2]) - 1
            x, y = merged[r][c]
            tmp = table[x][y]
            for i in range(50):
                for j in range(50):
                    if merged[i][j] == (x, y):
                        merged[i][j] = (i, j)
                        table[i][j] = "EMPTY"
            table[r][c] = tmp
            
        else:
            r, c = int(com[1]) - 1, int(com[2]) - 1
            x, y = merged[r][c]
            answer.append(table[x][y])
            
    return answer