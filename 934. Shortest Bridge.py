class Solution(object):
    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        
        def dfs(i,j,A):
            if i<0 or j<0 or i>=len(A) or j>=len(A[0]) or A[i][j]!=1:
                return
            A[i][j]=2
            dfs(i+1,j,A)
            dfs(i-1,j,A)
            dfs(i,j+1,A)
            dfs(i,j-1,A)
        
        island = 0
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j]==1:
                    dfs(i,j,A)
                    island = 1
                if island==1:
                    break
            if island==1:
                break
        
        print(A)
        step = 2
        d = [[0,-1],[0,1],[1,0],[-1,0]]
        while step-1 <= max(len(A), len(A[0])):
            # print(A)
            for i in range(len(A)):
                for j in range(len(A[0])):
                    if A[i][j]==step:
                        for ne in d:
                            ni,nj=ne[0]+i,ne[1]+j
                            # print(i,j, ne, ni,nj)
                            if ni<0 or nj<0 or ni>=len(A) or nj>=len(A[0]) or (A[ni][nj]<=step and A[ni][nj]>1):
                                continue
                            if A[ni][nj]==1:
                                return step-2
                            else:
                                A[ni][nj]=step+1
                                
            step +=1
s=Solution()
A = [[0,1],[1,0]]
A =[[0,1,0],[0,0,0],[0,0,1]]
A =[[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
s.shortestBridge(A)

d = [[0,-1],[0,1],[1,0],[-1,0]]
for ne in d:
    print(ne)