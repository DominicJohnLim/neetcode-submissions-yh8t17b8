class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1 for i in range(n + 1)]
        def dfs(current):
            if current >= n:
                return current == n
                
            if dp[current] != -1:
                return dp[current]
            
            dp[current] = dfs(current + 1)+dfs(current+2)
            return dp[current]


        
        
        return dfs(0)