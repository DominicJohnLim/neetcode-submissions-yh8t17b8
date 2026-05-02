import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        for stone in stones:
            heapq.heappush_max(heap, stone)
        

        while len(heap) > 1:
            first = heapq.heappop_max(heap)
            second = heapq.heappop_max(heap)
            if first > second:
                heapq.heappush_max(heap, first - second)
            elif first < second:
                heapq.heappush_max(heap, second - first)

        if len(heap) == 0:
            return 0
        else:
            return heap[0]