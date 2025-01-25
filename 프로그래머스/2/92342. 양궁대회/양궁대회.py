def solution(n, info):
    answer = []
    ryan = [0] * 11  # Ryan's arrow distribution
    max_diff = 0  # To track the max score difference

    def dfs(depth, arrows_left):
        nonlocal max_diff, answer
        
        if depth == 11:  # If we've assigned arrows to all score positions
            if arrows_left > 0:
                ryan[10] += arrows_left  # Assign remaining arrows to the lowest score
            
            # Calculate scores
            ryan_score, apeach_score = 0, 0
            for i in range(11):
                if info[i] == 0 and ryan[i] == 0:
                    continue  # No points awarded if no one scores on this slot
                
                if ryan[i] > info[i]:
                    ryan_score += (10 - i)  # Ryan wins this score
                else:
                    apeach_score += (10 - i)  # Apeach wins this score

            # Update best score difference
            if ryan_score > apeach_score:
                diff = ryan_score - apeach_score
                if diff > max_diff:
                    max_diff = diff
                    answer = ryan[:]  # Copy Ryan's current distribution
                elif diff == max_diff:
                    # Choose lexicographically larger (i.e., prioritize lower scores)
                    if answer and ryan[::-1] > answer[::-1]: 
                        answer = ryan[:]
            
            if arrows_left > 0:
                ryan[10] -= arrows_left  # Reset for backtracking
            return
        
        # Case 1: Ryan tries to win this score by shooting `info[depth] + 1` arrows
        if arrows_left > info[depth]:  
            ryan[depth] = info[depth] + 1
            dfs(depth + 1, arrows_left - (info[depth] + 1))
            ryan[depth] = 0  # Backtrack

        # Case 2: Ryan skips this score position
        dfs(depth + 1, arrows_left)

    dfs(0, n)

    return answer if answer else [-1]
