class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(row, col):
            grid[row][col] = "0"
            
            for r, c in dirs:
                next_row = row + r
                next_col = col + c
                if next_row >= 0 and next_row < rows and next_col >= 0 and next_col < cols and grid[next_row][next_col] == "1":
                    dfs(next_row, next_col)                    

        count = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    dfs(row, col)
                    count += 1
        
        return count
        
