class Solution(object):
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        # d = [[2,1],[1,2],[-1,2],[-2,1],[-2,-1],[-1,-2],[1,-2],[2,-1]]
        # 0-> 4,6
        # 1-> 6,8
        # 2-> 7,9
        # 3-> 4,8
        # 4-> 0,3,9
        # 5-> X
        # 6-> 0,1,7
        # 7-> 2,6
        # 8-> 1,3
        # 9-> 2,4
        
        
        if N==1:
            return 10
        m = 10**9+7
        f = [[1]*N for _ in xrange(10)]
        for n in xrange(1,N):
            f[0][n]=(f[4][n-1]+f[6][n-1]) %m
            f[1][n]=(f[6][n-1]+f[8][n-1]) %m
            f[2][n]=(f[7][n-1]+f[9][n-1]) %m
            f[3][n]=(f[4][n-1]+f[8][n-1]) %m
            f[4][n]=(f[0][n-1]+f[3][n-1]+f[9][n-1]) %m
            f[5][n]=0
            f[6][n]=(f[0][n-1]+f[1][n-1]+f[7][n-1]) %m
            f[7][n]=(f[2][n-1]+f[6][n-1]) %m
            f[8][n]=(f[1][n-1]+f[3][n-1]) %m
            f[9][n]=(f[2][n-1]+f[4][n-1]) %m 
        # print(f)
        return sum([i[N-1] for i in f])%m 