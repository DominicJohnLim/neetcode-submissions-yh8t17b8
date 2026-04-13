from bisect import bisect_left

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            j = bisect_left(numbers, target - numbers[i])
            if j == len(numbers) or numbers[j] != target - numbers[i]:
                pass
            else:
                return [i+1,j+1]