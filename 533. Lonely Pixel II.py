picture =[['W', 'B', 'W', 'B', 'B', 'W'],    
 ['W', 'B', 'W', 'B', 'B', 'W'],    
 ['W', 'B', 'W', 'B', 'B', 'W'],    
 ['W', 'W', 'B', 'W', 'B', 'W']] 

N = 3
class Solution(object):
    def findBlackPixel(self, picture, N):
        """
        :type picture: List[List[str]]
        :type N: int
        :rtype: int
        """
        count = 0
        for c in zip(*picture):
            if c.count('B') != N:
                continue
            first = picture[c.index('B')]
            if first.count('B')!=N:
                continue
            if picture.count(first) !=N:
                continue
            count+=1
        return count*N     
s = Solution()
s.findBlackPixel(picture,N)