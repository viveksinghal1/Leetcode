class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        doesFirstColHasZero = False
        rowLength = len(matrix)
        colLength = len(matrix[0])
        
        for i in range(rowLength):
            if matrix[i][0] == 0:
                doesFirstColHasZero = True
            for j in range(1, colLength):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # print(matrix)
        
        for i in range(rowLength-1, -1, -1):
            for j in range(colLength-1, 0, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if doesFirstColHasZero:
                matrix[i][0] = 0