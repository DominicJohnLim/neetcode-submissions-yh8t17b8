import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        for item in nums:
            if len(self.heap) >= self.k and item > self.heap[0]:
                heapq.heappop(self.heap)
                heapq.heappush(self.heap, item)
            elif len(self.heap) < self.k:
                heapq.heappush(self.heap, item)
        
        
    def add(self, val: int) -> int:
        if len(self.heap) >= self.k and val > self.heap[0]:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)
        elif len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        

        return self.heap[0]
        
