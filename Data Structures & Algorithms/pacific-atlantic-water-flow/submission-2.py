class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        rows = len(heights)
        cols = len(heights[0])
        pacific = set() # Cells that can reach pacific
        atlantic = set() # Cells that can reach atlantic

        def dfs(row, col, visited):
            visited.add((row, col))
            for r, c in dirs:
                next_row, next_col = row + r, col + c
                if (next_row in range(rows) and next_col in range(cols) 
                    and (next_row, next_col) not in visited
                    and heights[row][col] <= heights[next_row][next_col]):
                    dfs(next_row, next_col, visited)

        # Search starting from top and bottom edges
        for col in range(cols):
            dfs(0, col, pacific) # Top edge
            dfs(rows - 1, col, atlantic) # Bottom edge

        # Search starting from left and right edges
        for row in range(rows):
            dfs(row, 0, pacific) # Left edge
            dfs(row, cols - 1, atlantic) # Right edge

        # Find cells that can reach both pacific and atlantic
        res = []
        for row in range(rows):
            for col in range(cols):
                if (row, col) in pacific and (row, col) in atlantic:
                    res.append((row, col))
        
        return res