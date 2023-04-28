from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        rows = len(grid)
        cols = len(grid[0])
        
        def bfs(r, c):
            neighbors = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            if grid[r][c] != '1':
                return False
            queue = deque()
            queue.append((r, c))
            while queue:
                r, c = queue.popleft()
                for neighbor in neighbors:
                    if r - neighbor[0] < 0 or r - neighbor[0] >= rows or c - neighbor[1] < 0 or c - neighbor[1] >= cols:
                        continue
                    if grid[r - neighbor[0]][c - neighbor[1]] == '1':
                        queue.append((r - neighbor[0],c - neighbor[1]))
                        grid[r - neighbor[0]][c - neighbor[1]] = '2' #marked as visited

            return True
            
            
        
        for r in range(rows):
            for c in range(cols):
                if bfs(r, c):
                    ans += 1
        return ans

        

            
            
        