class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        steps = M * N
        visited = set()

        def findPaths(row, col, steps):
            if row < 0 or row >= M or col < 0 or col >= N or grid[row][col] == -1 or (row, col) in visited:
                return 0

            if grid[row][col] == 2 and steps == 0 :
                return 1
            
            visited.add((row, col))

            total = findPaths(row + 1, col, steps - 1) +\
                    findPaths(row - 1, col, steps - 1) +\
                    findPaths(row, col + 1, steps - 1) +\
                    findPaths(row, col - 1, steps - 1)

            visited.remove((row, col))

            return total

        for r in range(M):
            for c in range(N):
                if grid[r][c] == -1:
                    steps -= 1

        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    return findPaths(i, j, steps - 1)
