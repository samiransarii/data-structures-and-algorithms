class Solution:
    def totalNQueens(self, n: int) -> int:
        def isValid(r, c, board):
            # Check upward
            for i in range(r-1, -1, -1):
                if board[i][c] == "Q":
                    return False

            # Check left diagnol upward
            for i, j in zip(range(r-1, -1, -1), range(c-1, -1, -1)):
                if board[i][j] == "Q":
                    return False

            # Check right diagnol upward
            for i, j in zip(range(r-1, -1, -1), range(c+1, n)):
                if board[i][j] == "Q":
                    return False

            return True

        def solve(row, board):
            nonlocal count
            if row >= n:
                count += 1
                return

            for col in range(n):
                if isValid(row, col, board):
                    board[row][col] = "Q"
                    solve(row + 1, board)
                    board[row][col] = "."


        board = [["." for _ in range(n)] for _ in range(n)]
        count = 0
        solve(0, board)
        return count