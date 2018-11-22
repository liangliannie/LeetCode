class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        
        
        for i in range(len(matrix)-1):
            if matrix[i][0]<= target and matrix[i+1][0]>target:
                row = i
                break
        else:
            if target in matrix[len(matrix)-1]:
                return True
            else:
                return False
                
            
        if target in  matrix[row]:
            return True
        else:
            return False