class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        visited = set()

        def findPaths(row, col):
            if row < 0 or row >= m or col < 0 or col >= n:
                return 0

            if obstacleGrid[row][col] == 1 or (row, col) in visited:
                return 0

            if row == m - 1 and col == n - 1:
                return 1

            if dp[row][col] != -1:
                return dp[row][col]

            visited.add((row, col))

            dp[row][col] = findPaths(row + 1, col) + findPaths(row, col + 1)

            visited.remove((row, col))

            return dp[row][col]

        return findPaths(0, 0)

            
        