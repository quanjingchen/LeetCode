class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        neighbours = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        rows = len(board)
        cols = len(board[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        
        def dfs(index, r, c):
            # check the bottom case
            if index == len(word):
                return True

            # check the boundaries and if the cell is not visited:
            if isValid(r , c) and board[r][c] == word[index]:
                # mark the current cell
                visited[r][c] = True  
                # explore the neighbours:
                for neighbor in neighbours:
                    if dfs(index + 1, r + neighbor[0], c + neighbor[1]):
                        #visited[r][c] = False  # Reset visited cell when found
                        return True
                visited[r][c] = False  
            return False
        
        def isValid(x, y):
            if x < 0 or y < 0 or x >= rows or y >= cols:
                return False
            if visited[x][y] == True:
                return False
            return True
        
        
        for r in range(rows):
            for c in range(cols):
                if dfs(0, r, c):
                    return True
        return False
