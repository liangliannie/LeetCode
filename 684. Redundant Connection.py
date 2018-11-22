# class DSU(object):
#     def __init__(self):
#         self.par = range(10001)
#         self.rank = [0]*10001
#     def find(self,x):
#         while self.par[x] != x:
#             self.par[x] = self.find[self.par(x)]
#         return self.par[x]
#     def union(self,x,y):
#         xr,yr = self.find(x), self.find(y)
#         if xr==yr:
#             return False
#         elif self.rank[xr]<self.rank[yr]:
#             self.par[xr] = yr
#         elif self.rank[xr]>self.rank[yr]:
#             self.par[yr]= xr
#         else:
#             self.par[yr]=xr
#             self.rank[xr]+=1
#         return True
    
class DSU(object):
    def __init__(self):
        self.par = range(1001)
        self.rnk = [0] * 1001

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        elif self.rnk[xr] < self.rnk[yr]:
            self.par[xr] = yr
        elif self.rnk[xr] > self.rnk[yr]:
            self.par[yr] = xr
        else:
            self.par[yr] = xr
            self.rnk[xr] += 1
        return True

class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        import collections
        graph = collections.defaultdict(set)
        
        def dfs(u,v):
            if u==v: return True
            visited.add(u)
            return any(dfs(nei,v) for nei in graph[u]-visited)
                
 
        for u,v in edges:
            visited = set()
            print(visited)
            if u in graph and v in graph and dfs(u,v):
                print('uv')
                return u,v
            graph[u].add(v)
            graph[v].add(u)
            
f=Solution()
edges=[[1,2],[2,3],[2,4],[4,5],[1,5]]
f.findRedundantConnection(edges)