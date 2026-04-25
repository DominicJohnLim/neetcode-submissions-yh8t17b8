class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = [0 for i in range(len(nums))]

        for i in range(len(nums)):
            if seen[nums[i]] == 0:
                seen[nums[i]] = 1
            else:
                return nums[i]