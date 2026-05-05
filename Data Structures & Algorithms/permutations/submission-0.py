class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        
        def dfs(cur):
            nonlocal output

            if len(cur) == len(nums):
                output.append([])
                for i in cur:
                    output[-1].append(nums[i])
                return

            for i in range(len(nums)):
                if i not in cur:
                    x = cur.copy()
                    x.append(i)
                    dfs(x)
        
        dfs([])

        return output