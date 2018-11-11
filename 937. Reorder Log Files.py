class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        L = []
        for l in logs:
            L.append(l.split(' ')) 
            
        L = sorted(L, key=lambda l: l[1:] if ord(l[1][0]) > ord('A') else '{}') 
        
        LL = []
        for l in L:
            LL.append(' '.join(l))
        return LL