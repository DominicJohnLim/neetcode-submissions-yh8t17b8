class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = nums.count(0)

        if zero_count > 1:
            return [0 for i in range(len(nums))]
        elif zero_count == 1:
            single = 1
            index = -1
            for idx, item in enumerate(nums):
                if item != 0:
                    single *= item
                else:
                    index = idx
            output = [0 for i in range(len(nums))]
            output[index] = single
            
            return output
        else:
            total = 1
            for item in nums:
                total *= item

            return [total // item for item in nums]