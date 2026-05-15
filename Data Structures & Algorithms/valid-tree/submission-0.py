class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {i: [] for i in range((n))}
        visited = [False for i in range((n))]
        full = [True for i in range(n)]

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        def dfs(node, parent):
            visited[node] = True

            for edge in graph[node]:
                if edge == parent:
                    continue
                if visited[edge] or not dfs(edge, node):
                    return False
            
            return True
        
        return dfs(0, -1) and visited==full