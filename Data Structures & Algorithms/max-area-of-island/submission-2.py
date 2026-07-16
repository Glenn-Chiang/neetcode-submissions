class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(row, col):
            area = 1
            grid[row][col] = 0
            for r, c in dirs:
                next_row, next_col = row + r, col + c
                if next_row >= 0 and next_row < rows and next_col >= 0 and next_col < cols and grid[next_row][next_col] == 1:
                    area += dfs(next_row, next_col)
            return area

        max_area = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    area = dfs(row, col)
                    max_area = max(max_area, area)
        
        return max_area