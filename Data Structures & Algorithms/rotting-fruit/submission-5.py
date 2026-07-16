from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        fresh_count = 0
        queue = deque()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row, col))
                if grid[row][col] == 1:
                    fresh_count += 1

        if fresh_count == 0:
            return 0

        time = 0
        while queue:
            queue_len = len(queue)
            for i in range(queue_len):
                row, col = queue.popleft()
                for r, c in dirs:
                    next_row, next_col = row + r, col + c
                    if next_row >= 0 and next_row < rows and next_col >= 0 and next_col < cols:
                        if grid[next_row][next_col] == 1:
                            grid[next_row][next_col] = 2  
                            queue.append((next_row, next_col))
            time += 1

        # Check if there are any fresh fruits left
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return -1

        return time - 1
