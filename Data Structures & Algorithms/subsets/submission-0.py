class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # get first

        num = 0
        count = 0
        for i in nums:
            num = num | (1 << (i + 10))
            count += 1
        
        output = [num]

        for i in reversed(range(len(nums))):
            idx = nums[i] + 10
            add = []
            for j in output:
                bit = (j >> idx) & 1
                if bit:
                    add.append(j ^ (1 << idx))
            
            output.extend(add)

        true_output = []
        for o in output:
            true_output.append([i - 10 for i in range(o.bit_length()) if (o >> i) & 1])

        return true_output