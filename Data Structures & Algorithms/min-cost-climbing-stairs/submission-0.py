class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        
        output = 1000000
        
        for i in [0, 1]:
            dp = [-1 for i in range(n + 1)]
            def dfs(current):
                if current >= n:
                    if current == n:
                        return 0
                    return 1000000
                
                if dp[current] != -1:
                    return dp[current]
                
                dp[current] = cost[current] + min(dfs(current + 1), dfs(current + 2))

                return dp[current]
            dfs(i)
            output = min(dp[i], output)
        
        return output