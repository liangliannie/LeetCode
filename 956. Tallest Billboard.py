class Solution(object):
    def tallestBillboard(self, rods):
        """
        :type rods: List[int]
        :rtype: int
        """
        def make(A):
            states = {(0, 0)}
            for x in A:
                states |= ({(a+x, b) for a, b in states} |
                           {(a, b+x) for a, b in states})
            
            delta = {}
            for a,b in states:
                delta[a-b] = max(delta.get(a-b,0), a)
            return delta
        n = len(rods)
        lmake = make(rods[:n/2])
        rmake = make(rods[n/2:])
        
        ans = 0
        for d in lmake:
            if -d in rmake:
                ans = max(ans, lmake[d]+rmake[-d])
        return ans
#         dp = {0: 0}
#         for x in rods:
#             print(x, dp.items())
#             for d, h in list(dp.items()):
#                 dp[d + x] = max(dp.get(d + x, 0), h)
#                 dp[abs(d - x)] = max(dp.get(abs(d - x), 0), h + min(d, x))
#         return dp[0] 

s=Solution()
print(s.tallestBillboard([1,2,3,6]))