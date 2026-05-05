class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        nums.sort()

        def dfs(node, current):
            nonlocal output
            for i in nums:
                if node - i == 0:
                    output.append(current + [i])
                    break
                elif node - i > 0:
                    dfs(node - i, current + [i])
            
        dfs(target, [])

        return [list(i) for i in set([tuple(sorted(i)) for i in output])]