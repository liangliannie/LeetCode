picture = [["W","W","B"],["W","B","W"],["B","W","W"]]
# picture = [["1","2","3"],["4","5","6"],["7","8","9"]]

class Solution(object):
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
 
        picture_per =   [list(i) for i in zip(*picture)]
        R = [0]*len(picture)
        C = [0]*len(picture_per)
        for i, r in enumerate(picture):
            R[i]=r.count('B')
        for j, c in enumerate(zip(*picture)):
            C[j]=c.count('B')
                 
        count = 0
        for i in range(len(picture)):
            for j in range(len(picture[0])):
                if picture[i][j]=='B':
                    if R[i]==1 and C[j]==1:
                        count+=1
        return count

s = Solution()
ji=s.findLonelyPixel(picture)
print(ji)
