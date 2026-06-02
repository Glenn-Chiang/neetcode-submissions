class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0

        def dfs(row: int, col: int):
            if row < 0 or row >= len(grid):
                return
            if col < 0 or col >= len(grid[0]):
                return
            if grid[row][col] == "0":
                return

            grid[row][col] = "0"

            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dir in directions:
                dfs(row + dir[0], col + dir[1])
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "0":
                    continue
                dfs(i, j)
                count += 1
        return count
        
    