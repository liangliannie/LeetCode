

def minFallingPathSum(A):
    """
    :type A: List[List[int]]
    :rtype: int
    """
    m = len(A)
    n = len(A[0])
    
    dp = [['inf']*n ] 
         
minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]])