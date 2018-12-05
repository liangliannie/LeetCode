class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        def minpath(i,j, path=None):
            if path is None:
                path = A[i][j]
            if i==len(A)-1:
                yield path
                return
            for d in [-1,0,1]:
                if j+d>=0 and j+d<len(A[0]):
                    for bar in minpath(i+1,j+d,path+A[i+1][j+d]):
                        yield bar
                
        res =[]
        for j in range(len(A[0])):
            s = minpath(0,j)
            for i in s:
                res.append(i)
        return min(res)
s=Solution()    
s.minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]])


class Solution2(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        dp = [[0]*len(A[0]) for _ in xrange(len(A))]
        
        for r in xrange(len(A)-1,-1,-1):
            for c in xrange(len(A[0])):
                if r==len(A)-1:
                    dp[r][c]=A[r][c]
                else:
                    if c+1< len(A[0]) and c-1>=0:
                        dp[r][c]= A[r][c]+min(dp[r+1][c],dp[r+1][c+1],dp[r+1][c-1])
                    elif c+1< len(A[0]):
                        dp[r][c]= A[r][c]+min(dp[r+1][c],dp[r+1][c+1])
                    elif c-1>= 0:
                        dp[r][c]= A[r][c]+min(dp[r+1][c],dp[r+1][c-1])
                    else:
                        dp[r][c]= A[r][c]+min(dp[r+1][c])
        # print(dp)
        return min(dp[0])