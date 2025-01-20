class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row = len(matrix)
        col = len(matrix[0])
        output = []
        
        # 0 = left to right
        # 1 = top to bottom
        # 2 = right to left
        # 3 = bottom to top
        direction = 0

        top = 0
        bottom = row - 1
        left = 0
        right = col - 1

        while top <= bottom and left <= right:

            if direction == 0:
                # top is constant
                for i in range(left, right + 1):
                    output.append(matrix[top][i])

                top += 1

            if direction == 1:
                # right is constant
                for i in range(top, bottom + 1):
                    output.append(matrix[i][right])

                right -= 1

            if direction == 2:
                # bottom is constant
                for i in range(right, left - 1, -1):
                    output.append(matrix[bottom][i])

                bottom -= 1

            if direction == 3:
                # left is contant
                for i in range(bottom, top - 1, -1):
                    output.append(matrix[i][left])

                left += 1

            direction += 1
            if direction >= 4:
                direction = 0

        return output