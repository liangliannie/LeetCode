class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        res = 0
        row = [False]*(len(A)-1)
  
        for col in range(len(A[0])):
            if all(row[i] or A[i][col]<=A[i+1][col] for i in range(len(A)-1)):
                
                for i in xrange(len(A)-1):
                    # print(row, row[i], A[i][col], A[i+1][col])
                    if A[i][col]<A[i+1][col]:
                        row[i] = True
            else:
                res +=1

        return res
            