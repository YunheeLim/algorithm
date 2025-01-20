def solution(alp, cop, problems):    
    max_alp = max([problems[i][0] for i in range(len(problems))])
    max_cop = max([problems[i][1] for i in range(len(problems))])

    if max_alp < alp:
        alp = max_alp
    if max_cop < cop:
        cop = max_cop
        
    dp = [[151 for i in range(max_cop + 1)] for j in range(max_alp + 1)]
    dp[alp][cop] = 0
    
    for i in range(alp, max_alp + 1):
        for j in range(cop, max_cop + 1):
            if i + 1 <= max_alp:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + 1)
            
            if j + 1 <= max_cop:
                dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + 1)
            
            for p in problems:
                alp_req, cop_req, alp_rwd, cop_rwd, cost = map(int, p)
                if alp_req <= i and cop_req <= j:
                    next_alp = min(max_alp, i + alp_rwd)
                    next_cop = min(max_cop, j + cop_rwd)
                    dp[next_alp][next_cop] = min(dp[next_alp][next_cop], dp[i][j] + cost)
                    
    return dp[-1][-1]