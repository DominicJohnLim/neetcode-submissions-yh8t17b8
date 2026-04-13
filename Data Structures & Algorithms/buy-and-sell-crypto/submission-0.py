class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest = 101
        output = 0

        for i in range(len(prices)):
            output = max(output, prices[i] - smallest)
            smallest = min(smallest, prices[i])
        
        return output