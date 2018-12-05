class Solution(object):
    def movesToStamp(self, s, t):
        """
        :type stamp: str
        :type target: str
        :rtype: List[int]
        """
        if s[0] != t[0] or s[-1] != t[-1]: return []
        n, m = len(s), len(t)