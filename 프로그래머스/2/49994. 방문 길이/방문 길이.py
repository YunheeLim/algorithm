def solution(dirs):
    dic = {"U": 0, "D": 1, "R": 2, "L": 3}
    dx = [0, 0, 1, -1]  # Right, Left are horizontal moves
    dy = [1, -1, 0, 0]  # Up, Down are vertical moves
    visited = set()
    
    x, y = 0, 0  # Start at the origin
    answer = 0

    for dir in dirs:
        nx = x + dx[dic[dir]]
        ny = y + dy[dic[dir]]

        if -5 <= nx <= 5 and -5 <= ny <= 5:  # Check if within bounds
            if (x, y, nx, ny) not in visited and (nx, ny, x, y) not in visited:
                visited.add((x, y, nx, ny))
                visited.add((nx, ny, x, y))  # Store reverse path
                answer += 1
            x, y = nx, ny  # Move to the next position

    return answer
