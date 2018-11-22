# from platform import node
class DSU(object):
    def __init__(self, m, n):
        all_ = m*n
        self.par = range(all_)
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
        dic = DSU(m,n)
        count = 0
        list_ = []
        for i, node in enumerate(positions):
            x,y = node
            past_points=positions[:i+1]
            if [x+1,y] in past_points and x+1<m:
                dic.union((x*n+y), (x+1)*n+y)
            if [x-1,y] in past_points and x-1>=0:
                dic.union((x*n+y), (x-1)*n+y)
            if [x,y+1] in past_points and y+1<n:
                dic.union((x*n+y), (x)*n+y+1)
            if [x,y-1] in past_points and y-1>=0:
                dic.union((x*n+y), (x)*n+y-1)
            ll=set()
            for node1 in past_points:
                x1,y1 = node1
                ll.add(dic.find(x1*n+y1))                    
            list_.append(len(ll))
        return (list_)
            
            
            

                    
                
                
#         for i in list_:
#             print(i)    
f = Solution()
positions = [[0,0], [0,1], [1,2], [2,1]]
l=f.numIslands2(3, 3, positions)
print(l)

positions = [[0,0],[1,1],[0,1]]
l=f.numIslands2(2, 2, positions)

print(l)
# positions = [[0,1], [0,0]]
# f.numIslands2(1, 2, positions)