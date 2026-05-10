class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        INF = 2147483647
        output = [[0 for i in range(len(grid[j]))] for j in range(len(grid))]

        def flood(x,y,dist):
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == -1:
                return

            if grid[x][y] >= dist:
                grid[x][y] = dist
            
                flood(x - 1,y,dist+1)
                flood(x + 1,y,dist+1)
                flood(x,y - 1,dist+1)
                flood(x,y + 1,dist+1)

            

        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == 0:
                    flood(x,y,0)
        
        # print(grid)