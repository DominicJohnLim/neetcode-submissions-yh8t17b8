class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        output = 0
        visited = [False for i in range(n)]

        adj = [[] for i in range(n)]

        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        def dfs(node):
            if visited[node]:
                return
            
            visited[node] = True
            for x in adj[node]:
                dfs(x)
    
        for i in range(n):
            if not visited[i]:
                dfs(i)
                output += 1
        
        return output