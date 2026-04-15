class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        combined = sorted([(position[i], speed[i]) for i in range(len(speed))], reverse=True)

        distance_mph = [(target - item[0]) / item[1] for item in combined]
        

        # print(distance_mph)
        current_heap = []
        counter = 1

        for i in range(len(speed)):
            if len(current_heap) > 0 and current_heap[0] >= distance_mph[i]:
                heapq.heappush_max(current_heap, distance_mph[i])
            elif len(current_heap) > 0:
                current_heap = []
                counter += 1
            
            if len(current_heap) == 0:
                heapq.heappush(current_heap, distance_mph[i])
            
            # print(current_heap)
        
        return counter
        
