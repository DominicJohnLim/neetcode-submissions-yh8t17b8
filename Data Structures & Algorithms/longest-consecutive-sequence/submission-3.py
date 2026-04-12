class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        pointer = 0

        # print(sorted(nums))
        nums = sorted(list(set(nums)))
        # print(nums)

        for i in range(1, len(nums)):
            first, second = nums[pointer], nums[i]
            if second != first + (i - pointer):
                longest = max(longest, i - pointer)
                pointer = i
            
            print(first, second, longest, pointer, i-pointer)
        
        return max(longest, len(nums) - pointer)