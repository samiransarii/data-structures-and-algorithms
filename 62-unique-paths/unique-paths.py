class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for _ in range(n)] for _ in range(m)]

        def findPath(row, col):
            if row >= m or col >= n:
                return 0

            if dp[row][col] != -1:
                return dp[row][col]
            
            if row == m - 1 and col == n - 1:
                return 1

            total = findPath(row + 1, col) + findPath(row, col + 1) # down + left paths

            dp[row][col] = total

            return total

        return findPath(0, 0)