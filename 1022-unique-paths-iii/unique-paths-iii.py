class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        walkable = 0
        start_r = start_c = -1
        visited = set()

        def findPaths(row, col, remain):
            if row < 0 or row >= M or col < 0 or col >= N or grid[row][col] == -1 or (row, col) in visited:
                return 0

            if grid[row][col] == 2:
                return 1 if remain == 1 else 0
            
            visited.add((row, col))

            total = (findPaths(row + 1, col, remain - 1) +
                    findPaths(row - 1, col, remain - 1) +
                    findPaths(row, col + 1, remain - 1) +
                    findPaths(row, col - 1, remain - 1))

            visited.remove((row, col))

            return total

        for r in range(M):
            for c in range(N):
                if grid[r][c] != -1:
                    walkable += 1
                if grid[r][c] == 1:
                    start_r, start_c = r, c

        return findPaths(start_r, start_c, walkable)
