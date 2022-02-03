class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        low = 0
        high = m*n - 1
        while low <= high:
            mid = (low + high) // 2
            
            if (matrix[mid//m][mid%m] == target):
                return True
            elif matrix[mid//m][mid%m] < target:
                low = mid + 1
            else:
                high = mid - 1
                
                
        return False
        