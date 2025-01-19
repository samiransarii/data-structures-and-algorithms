class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        output = []
        board = [['.' for _ in range(n)] for _ in range(n)]

        def isValid(r, c, board):
            # Check in upper direction
            for i in range(r-1, -1, -1):
                if board[i][c] == "Q":
                    return False

            # Check left diagnol
            for i, j in zip(range(r-1, -1, -1), range(c-1, -1, -1)):
                if board[i][j] == "Q":
                    return False

            # Check right diagnol
            for i, j in zip(range(r-1, -1, -1), range(c+1, n)):
                if board[i][j] == "Q":
                    return False

            return True
        
        def solve(row, board):
            nonlocal output
            if row >= n:
                solution = ["".join(row) for row in board]
                output.append(solution)
                return

            for col in range(n):
                if isValid(row, col, board):
                    board[row][col] = "Q"
                    solve(row + 1, board)
                    board[row][col] = "."

        solve(0, board)
        return output
        