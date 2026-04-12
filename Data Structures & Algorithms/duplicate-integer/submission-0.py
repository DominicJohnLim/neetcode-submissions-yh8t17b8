class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_hash = {}
        for item in nums:
            if item not in count_hash:
                count_hash[item] = 1
            else:
                return True

        return False