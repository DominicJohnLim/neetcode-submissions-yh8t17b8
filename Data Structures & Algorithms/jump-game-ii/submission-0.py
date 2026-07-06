class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [1000000000 for i in range(len(nums))]

        q = [0]
        dp[0] = 0

        while len(q):
            top = q.pop()
            # print(top)

            for i in range(1, nums[top] + 1):
                x = i + top
                # if x < len(nums): print("lol", x, nums[top], dp[x], dp[top])
                if x < len(nums) and dp[x] > dp[top] + 1:
                    q.append(x)
                    dp[x] = dp[top] + 1
        
        return dp[-1]
