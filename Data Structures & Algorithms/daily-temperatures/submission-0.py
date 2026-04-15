class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        results = [0] * len(temperatures)

        for i in range(len(temperatures)):
            current = temperatures[i]
            # if len(stack) > 0: print(stack, current, current > stack[0][0])
            while len(stack) > 0 and current > stack[0][0]:
                idx = heapq.heappop(stack)[1]
                results[idx] = i - idx
                # print(stack)
            
            heapq.heappush(stack, (current, i))

        
        return results