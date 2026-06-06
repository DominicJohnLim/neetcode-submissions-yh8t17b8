class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1 for i in range(len(nums))]

        def dfs(idx):
            if idx == len(nums):
                return 0
            
            if dp[idx] != -1:
                return dp[idx]

            
            best = 0
            for i in range(idx + 2, len(nums)):
                best = max(best, dfs(i))
            
            dp[idx] = nums[idx] + best

            return dp[idx]

        
        dfs(0)

        output = max(dp)
        dp = [-1 for i in range(len(nums))]
        
        dfs(1)
        return max(output, max(dp))