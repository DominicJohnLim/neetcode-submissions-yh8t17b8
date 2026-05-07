class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        done = False
        visited = [[False for i in range(len(board[0]))] for j in range(len(board))]

        def flood(x, y, idx):
            nonlocal done
            if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or idx >= len(word) or visited[x][y] or board[x][y] != word[idx] or done:
                return False
            
            # print(x,y,idx, word[idx], board[x][y])

            if idx == len(word) - 1 and board[x][y] == word[idx]:
                done = True
                return True
            visited[x][y] = True
            res = (flood(x - 1, y, idx + 1) or
                  flood(x + 1, y, idx + 1) or
                  flood(x, y - 1, idx + 1) or
                  flood(x, y + 1, idx + 1))
            visited[x][y] = False

            return res



        for x in range(len(board)):
            for y in range(len(board[x])):
                visited = [[False for i in range(len(board[0]))] for j in range(len(board))]
                if flood(x,y,0):
                    return True
        

        return done