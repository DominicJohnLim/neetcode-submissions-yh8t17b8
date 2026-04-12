class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup_hash = {} 
        for index, item in enumerate(nums):

            if item in lookup_hash:
                return [lookup_hash[item], index]

            lookup_hash[target - item] = index