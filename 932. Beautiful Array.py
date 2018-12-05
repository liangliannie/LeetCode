class Solution(object):
    def beautifulArray(self, N):
        """
        :type N: int
        :rtype: List[int]
        """
        res = [1]
        while len(res)<N:
            res = [i*2 for i in res]+[i*2-1 for i in res]
        return [i for i in res if i<=N]
    
    
    def beautifulArray2(self, N):
        return sorted(range(1, N + 1), key=lambda x: bin(x)[:1:-1])
s=Solution()
# for i in s.beautifulArray2(5):
#     print(i, bin(i)[:1:-1])
print(s.beautifulArray(9))