class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        # directions: up, down, left and right
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        # get the number of rows and columns
        rows = len(heights)
        cols = len(heights[0])
        # initilize variables, keep track of the cell which can reach the ocean
        memo_pac = set()
        memo_atl = set()
                
        
        def dfs(r, c, memo):
            #get the height of the current cell
            h = heights[r][c]
            # mark the current cell to be visted
            memo.add((r, c))
            # start the recursion
            for dir in dirs:
                r_next = r + dir[0]
                c_next = c + dir[1]
                if r_next < 0 or r_next >= rows or c_next < 0 or c_next >= cols or (r_next, c_next) in memo or heights[r_next][c_next] < h:
                    continue
                dfs(r_next, c_next, memo)
            
        # iterates throught each cell on the coast and start DFS
        for r in range(rows):
            dfs(r, 0, memo_pac)
            dfs(r, cols - 1, memo_atl)
            
        for c in range(cols):
            # dfs traversal for the current cell
            dfs(0, c, memo_pac)
            dfs(rows - 1, c, memo_atl)         
            
        return list(memo_pac.intersection(memo_atl))
            
            
            
            
            
            
            
            
            
        