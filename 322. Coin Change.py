class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
    
        dp = [0]+[-1]*amount
        for i in xrange(1,amount+1):
            l = []
            for c in coins:
                if i-c>=0  and dp[i-c]>=0:
                    l.append(dp[i-c])
#             print(l)
            if len(l)>0:
                dp[i] = min(l)+1
            
#         print(dp)
        return dp[-1]
coins = [1, 2, 5]
amount = 11
coins =[2]
amount =3
s=Solution()
s.coinChange(coins,amount)
print(s)