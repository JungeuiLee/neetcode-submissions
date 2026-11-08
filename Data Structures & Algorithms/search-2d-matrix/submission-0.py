class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # for i in range(len(matrix)):
        #     if matrix[i][0] <= target <= matrix[i][-1]:
        
        m = len(matrix)
        n = len(matrix[0])
        left = 0
        right = (m * n )-1

        while left <= right:
            middle = (left+right )//2
            
            if matrix[middle // n][middle % n] == target:
                return True
            
            elif matrix[middle // n][middle % n] <= target:
                left = middle+1
            else:
                right = middle-1
        return False
