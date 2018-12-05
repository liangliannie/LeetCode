import collections
class Solution(object):
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        
        if len(p)<=1:
            return len(p)
        p,l,count = '*'+p,0,collections.Counter()
        for i in xrange(1,len(p)):
            if p[i-1]+p[i] not in 'zabcdefghijklmnopqrstuvwxyz':
                l=i
            count[p[i]] = max(count[p[i]], i-l+1)
        return sum(count.values())
            