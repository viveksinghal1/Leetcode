class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrixLength = len(matrix)
        
        for i in range(matrixLength):
            for j in range(i):
                self.swap(matrix, i, j)
                
        for i in range(matrixLength):
            for j in range(matrixLength//2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][matrixLength-j-1]
                matrix[i][matrixLength-j-1] = temp
        
        
    def swap(self, matrix: List[List[int]], i: int, j: int) -> None:
        temp = matrix[i][j]
        matrix[i][j] = matrix[j][i]
        matrix[j][i] = temp