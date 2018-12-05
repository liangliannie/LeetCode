# from platform import node
class DSU(object):
    def __init__(self, m, n):
        all_ = m*n
        self.par = [-1]*all_
        self.rnk = [0]*all_
    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    def union(self, x, y): 
        xr,yr = self.find(x), self.find(y)
        if xr != yr:
            if self.rnk[xr] > self.rnk[yr]:
                self.par[yr] = xr 
            elif self.rnk[xr] < self.rnk[yr]:
                self.par[xr] = yr
            else:
                self.par[yr] = xr 
                self.rnk[xr] +=1
                                

                
class Solution(object):         
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        par = [-1]*(m*n)
        rnk = [0]*(m*n)

        def find(x):
            if par[x] != x:
                par[x] = find(par[x])
            return par[x]
        
        def union(x, y): 
            xr,yr = find(x), find(y)
            if xr != yr:
                if rnk[xr] > rnk[yr]:
                    par[yr] = xr 
                elif rnk[xr] < rnk[yr]:
                    par[xr] = yr
                else:
                    par[yr] = xr 
                    rnk[xr] +=1
        cnt = 0
        res = []
        for i, node in enumerate(positions):
            x,y = node
            value = x*n+y
            if par[value] == -1:
                par[value] = value
                cnt +=1
                
            if  x+1<m and par[value+n] != -1:
                if find(value) != find(value+n):
                    union(value, value+n)
                    cnt -=1
            if  x-1>=0 and par[value-n] != -1:
                if find(value) != find(value-n):
                    union(value, value-n)
                    cnt -=1
            if  y+1<n and par[value+1]  != -1:
                if find(value) != find(value+1):
                    union(value, value+1)
                    cnt -=1
            if  y-1>=0 and par[value-1] != -1:
                if find(value) != find(value-1):
                    union(value, value-1)
                    cnt -=1
            res.append(cnt)
       
        return res
                        

                    
                
                
#         for i in list_:
#             print(i)    
f = Solution()
positions = [[0,0], [0,1], [1,2], [2,1]]
l=f.numIslands2(3, 3, positions)
print(l)

positions = [[0,0],[1,1],[0,1]]
l=f.numIslands2(2, 2, positions)


positions = [[8,5],[8,0],[3,4],[0,3],[1,0],[5,4],[0,8],[5,7],[0,6],[6,2],[4,7],[2,7],[8,7],[8,6],[5,3],[2,3],[3,5],[3,1],[0,2],[8,8],[6,4],[0,1],[0,4],[7,5],[3,0]]
l=f.numIslands2(9, 9, positions)
print(l)
# positions = [[0,1], [0,0]]
# f.numIslands2(1, 2, positions)