class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(row, col):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                return 0
            if grid[row][col] == 0:
                return 0
            
            grid[row][col] = 0

            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            area = 1
            for dir in directions:
                area += dfs(row + dir[0], col + dir[1])
            return area

        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    continue
                max_area = max(max_area, dfs(i, j))
        return max_area