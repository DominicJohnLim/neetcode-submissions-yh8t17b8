class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [100000000000 for i in range(n + 1)]

        adj = [[] for i in range(n + 1)]

        for time in times:
            adj[time[0]].append(time[1:])

        queue = []
        queue.append(k)
        dist[k] = 0
        dist[0] = 0
        
        while len(queue):
            top = queue.pop()

            for node, weight in adj[top]:
                if dist[node] > weight + dist[top]:
                    queue.append(node)
                    dist[node] = weight + dist[top]
        
        output = 0
        for i in dist:
            output = max(output, i)
            if i == 100000000000:
                output = -1
                break
        
        return output
        # if dist[]