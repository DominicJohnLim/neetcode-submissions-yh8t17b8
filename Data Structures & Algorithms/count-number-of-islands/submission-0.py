class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]

        def flood(x, y):
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or visited[x][y] or grid[x][y] == '0':
                return
            
            visited[x][y] = True
            flood(x - 1,y)
            flood(x + 1,y)
            flood(x,y - 1)
            flood(x,y + 1)

        output = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == '1' and not visited[x][y]:
                    flood(x, y)
                    output += 1

        return (output)