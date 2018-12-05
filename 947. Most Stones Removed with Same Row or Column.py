class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        visited=[False]*len(stones)
        import collections
        d = collections.defaultdict(set)
        for x, y in stones:
            d[x].add(y)
            d[y].add(x)
            
        def dfs(i, visited):
            visited[i] = True
            x,y = stones[i]
            for dx in d[x]:
                if [x,dx] in stones:
                    j = stones.index([x,dx])
                    if visited[j]==False:
                        dfs(j,visited)
                            
            for dy in d[y]:
                if [dy,y] in stones:
                    j = stones.index([dy,y])
                    if visited[j]==False:
                        dfs(j,visited)
            return
        
        
        cnt = 0
        for s in xrange(len(stones)):
            if visited[s]==False:
#                 print('cnt',cnt)
                dfs(s,visited)
                cnt+=1
        return(len(stones)-cnt)
                
stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
k = Solution()
print(k.removeStones(stones))
            
stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
k = Solution()
print(k.removeStones(stones))

stones = [[0,0]]
k = Solution()
print(k.removeStones(stones))
