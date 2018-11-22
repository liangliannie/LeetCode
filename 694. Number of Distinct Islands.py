class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def dfs(grid,i,j,i0,j0):
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] !=1:
                return
            shape.add((i-i0,j-j0))
            grid[i][j]=0

            dfs(grid, i+1,j,i0,j0)
            dfs(grid, i-1,j,i0,j0)
            dfs(grid, i,j+1,i0,j0)
            dfs(grid, i,j-1,i0,j0)
        
        shapes = set()
        for i in range(len(grid)):
            for j in range((len(grid[0]))):
                if grid[i][j]==1:
                    shape = set()
                    dfs(grid,i,j,i,j)
                    if shape:
                        shapes.add(frozenset(shape))
        # print(shapes)
        return len(shapes)
                