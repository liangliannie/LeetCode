import itertools
class Solution(object):
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        ans = -1
        res = []
        for h1, h2, m1, m2 in itertools.permutations(A):
            hours = 10 * h1 + h2
            mins = 10 * m1 + m2
            time = 60 * hours + mins
            if 0 <= hours < 24 and 0 <= mins < 60 and time > ans:
                ans = time
                res = [h1, h2, m1, m2]
            
        return str(res[0])+str(res[1])+":"+str(res[2])+str(res[3]) if ans>=0 else ""