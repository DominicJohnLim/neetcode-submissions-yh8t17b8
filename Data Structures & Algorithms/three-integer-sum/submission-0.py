class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = set()

        for i in range(len(nums)):
            if nums[i] > 0: 
                break

            possible = {}
            for j in range(i, len(nums)):
                possible[-(nums[i] + nums[j])] = j
            
            for j in range(i, len(nums)):
                if nums[j] in possible and j != possible[nums[j]] and j != i and i != possible[nums[j]]:
                    output.add(tuple(sorted((nums[i], nums[possible[nums[j]]], nums[j]))))
        return list(output)


