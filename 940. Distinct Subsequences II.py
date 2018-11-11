class Solution(object):
    def distinctSubseqII(self, S):
        """
        :type S: str
        :rtype: int
        """
        dp=[1]*len(S)
        d ={S[0]:0}
        m=10**9 + 7
        for i in range(1,len(S)):
            n=S[i]
            if n not in d:
                dp[i]=sum(dp[:i])+1 %m
            else:
                dp[i]=sum(dp[d[n]:i])%m
            d[n]=i
        return sum(dp)%m
    
f=Solution()

s= f.distinctSubseqII("aaa")
print(s)

s= f.distinctSubseqII("abaa")
print(s)

s= f.distinctSubseqII("abc")

print(s)
