def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        def Path(Seen, i, j):
            if i>=0 and i<=len(A)-1 and j>=0 and j<=len(A[0])-1:
                if i==len(A)-1:
                    return Seen
                else:
                    Path(Seen.append(A[i][j]),i+1,j-1)
                    Path(Seen.append(A[i][j]),i+1,j)
                    Path(Seen.append(A[i][j]),i+1,j+1)
                    
                    
                    
                    
minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]])