class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        decay = [[1000000 for i in range(len(grid[0]))] for j in range(len(grid))]

        def flood(x,y,time):
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 0:
                return
            
            if decay[x][y] >= time:
                decay[x][y] = time
                flood(x + 1,y,time+1)
                flood(x - 1,y,time+1)
                flood(x,y + 1,time+1)
                flood(x,y - 1,time+1)

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 2:
                    flood(x,y,0)
        
        output = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    if decay[x][y] == 1000000:
                        return -1
                    output = max(output, decay[x][y])
        
        return output