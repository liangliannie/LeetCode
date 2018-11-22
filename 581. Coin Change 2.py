class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [1]+[0]*amount
        
        for coin in coins:
            for m in xrange(amount+1):
                if m - coin>=0:
                    dp[m] += dp[m - coin]
        return dp[-1]
    
s=Solution()
amount = 5
coins = [1, 2, 5]
ss=s.change(amount, coins)
print(ss)