class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = []
        total = 0
        for i in nums:
            total += i
            dp.append(total)
        
        output = -10000000000
        local_smallest = 10000000000

        for i in range(len(dp)):
            local_smallest = min(local_smallest, dp[i])
            output = max(output, max(dp[i] - local_smallest, dp[i]))
            # print(local_smallest, output, dp[i])
        
        if output == 0: output = max(nums)

        return output