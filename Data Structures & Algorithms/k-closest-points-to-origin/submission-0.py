import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        queue = []

        for point in points:
            heapq.heappush(queue, (point[0]*point[0] + point[1]*point[1], point))

        output = []
        for i in range(k):
            output.append(heapq.heappop(queue)[-1])
        
        return output