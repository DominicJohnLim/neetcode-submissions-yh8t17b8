class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False for i in range(len(nums))]

        q = []
        q.append(0)

        while len(q):
            top = q.pop()
            dp[top] = True

            for i in range(1, nums[top] + 1):
                if top + i < len(nums) and not dp[i+top]:
                    q.append(i + top)
        
        return dp[-1]