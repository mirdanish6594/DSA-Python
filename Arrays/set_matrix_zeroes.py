from typing import List

class Solution:
    def setMatrixZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        first_row_has_zeroes = any(matrix[0][j] == 0 for j in range(cols))
        first_col_has_zeroes = any(matrix[i][0] == 0 for i in range(rows))

        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        if first_col_has_zeroes:
            for j in range(cols):
                matrix[0][j] = 0

        if first_col_has_zeroes:
            for i in range(rows):
                matrix[i][0] = 0


if __name__ == "__main__":
    m = int(input("Enter the no. of rows: "))
    n = int(input("Enter the no. of columns: "))

    print("Enter matrix row by row: ")
    matrix = [list(map(int, input().split())) for _ in range(m)]
    
    sol = Solution()
    sol.setMatrixZeroes(matrix)

    print("Modified Matrix:")
    for row in matrix: 
        print(row)

