class Solution(object):
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        import collections
        count = collections.Counter(A)
        deplicate = []
        ans = 0
        for x in xrange(100000):
            if count[x]>=2:
                deplicate.extend([x]*(count[x]-1))
            elif deplicate and count[x]==0:
                ans += x-deplicate.pop()
        return ans