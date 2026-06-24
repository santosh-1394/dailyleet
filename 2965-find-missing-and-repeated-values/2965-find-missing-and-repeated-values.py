class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        seen = set()
        repeated = -1

        for r in range(rows):
            for c in range(cols):
                value = grid[r][c]

                if value in seen:
                    repeated = value
                else:
                    seen.add(value)
        n = len(grid)

        for num in range(1, n * n + 1):
            if num not in seen:
                missing = num
        
        return [repeated, missing]