class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        o = 1
        e = 0
        while o<=len(A):
            # print(o,e,A)
            if A[o]%2 == 1:
                o+=2
                continue
            while e<=len(A):
                if A[e]%2 == 1:
                    break
                else:
                    e+=2
            t = A[e]
            A[e]=A[o]
            A[o]=t
            e,o = e+2,o+2
        return (A)
        
s=Solution()
print(s.sortArrayByParityII([4,2,5,7]))