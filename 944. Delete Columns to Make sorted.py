class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        res = 0
        for col in zip(*A):
            if all(col[i]<=col[i+1] for i in range(len(col)-1)):
                continue
            else:
                res +=1
        return res