class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        rows = len(heights)
        cols = len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(row, col, visited):
            if (row, col) in visited:
                return
            visited.add((row, col))
            for dir in directions:
                next_row = row + dir[0]
                next_col = col + dir[1]
                if next_row < 0 or next_col < 0 or next_row >= rows or next_col >= cols:
                    continue
                if heights[next_row][next_col] >= heights[row][col]:
                    dfs(next_row, next_col, visited)

        for col in range(cols):
            dfs(0, col, pacific)
            dfs(rows - 1, col, atlantic)
        for row in range(rows):
            dfs(row, 0, pacific)
            dfs(row, cols - 1, atlantic)

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])
        return res
        