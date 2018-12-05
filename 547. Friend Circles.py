class Solution2(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        visited = [False]*len(M)
        def dfs(i):
            visited[i] = True
            for j in range(len(M)):
                if M[i][j]==1 and not visited[j]:
                    dfs(j)
            # return
            
        cnt = 0
        for i in range(len(M)):
            if visited[i]: continue
            dfs(i)
            cnt +=1
        return cnt
    

class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        par = range(len(M))
        rnk = [0]*len(M)
        
        def find(x):
            if par[x] !=x:
                par[x] = find(par[x])
            return par[x]
        
        def union(x,y):
            xr,yr = find(x),find(y)
            if xr!=yr:
                if rnk[xr]>=rnk[yr]:
                    par[yr]=xr
                elif rnk[yr]>rnk[xr]:
                    par[xr]=yr
                else:
                    par[yr]=xr
                    rnk[xr]+=1
                    
        for i in range(len(M)):
            for j in range(i+1,len(M)):
          
                if M[i][j]==1:
                    p,q = find(i),find(j)
                    # print(i,j)
                    # print(par)
                    if p!=q:
                        par[p]=q
                        # union(i,j)
                    # print(par)
        res = set()   
        for i in range(len(M)):
            res.add(find(i))
            
        return len(res)