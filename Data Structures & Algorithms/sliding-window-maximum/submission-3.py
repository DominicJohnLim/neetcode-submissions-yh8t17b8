from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        heap = []
        q = deque()
        exit_queue = []

        for i in range(len(nums)):
            q.append(nums[i])
            heapq.heappush_max(heap, nums[i])
            # print(q, heap, exit_queue, output)

            if i >= k:
                remove = q.popleft()
                heapq.heappush_max(exit_queue, remove)

                # print(exit_queue)

                while len(exit_queue) > 0 and exit_queue[0] == heap[0]:
                    heapq.heappop_max(exit_queue)
                    heapq.heappop_max(heap)
                    # print(heap)
            if i >= k - 1:
                # print(heap[0])
                output.append(heap[0])
        # print(output)
        return output